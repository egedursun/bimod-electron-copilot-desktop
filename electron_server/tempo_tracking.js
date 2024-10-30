const moment = require('moment');
const screenshot = require('screenshot-desktop');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const fs = require('fs');
const uuid = require('uuid');
const axios = require('axios');
const FormData = require('form-data');

let isTrackingActive = false;
let screenshotJob = null;
let sendLogsJob = null;

// Base directory for media storage in Django project
const mediaBasePath = path.join(__dirname, '..', 'media', 'metatempo', 'logs');

// Server URL
const SERVER_BASE_URL = process.env.SERVER_BASE_URL;

// Fetch configuration settings from the database
async function getConfiguration() {
  return new Promise((resolve, reject) => {
    const dbPath = path.join(__dirname, '..', 'db.sqlite3');
    const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READONLY, (err) => {
      if (err) return reject(err);
    });

    db.get(`SELECT * FROM metatempo_board_connection ORDER BY created_at DESC LIMIT 1`, (err, row) => {
      db.close();
      if (err) reject(err);
      else resolve(row);
    });
  });
}

// Check if current time is within the allowed tracking window
function isWithinTrackingTime(config) {
  const now = moment();
  const startTime = moment(config.tracking_start_time, 'HH:mm');
  const endTime = moment(config.tracking_end_time, 'HH:mm');
  const today = moment().format('dddd');
  const weekdays = JSON.parse(config.tracked_weekdays || '[]');

  return weekdays.includes(today) && now.isBetween(startTime, endTime);
}

// Convert member_log_intervals to seconds for scheduling
function getIntervalSeconds(interval) {
  const intervals = {
    'times_12_per_hour': 5 * 60,
    'times_6_per_hour': 10 * 60,
    'times_4_per_hour': 15 * 60,
    'times_3_per_hour': 20 * 60,
    'times_2_per_hour': 30 * 60,
    'hourly': 60 * 60,
    'every_2_hours': 2 * 60 * 60,
    'every_4_hours': 4 * 60 * 60
  };
  return intervals[interval] || 10 * 60;
}

// Save log entry to the database
function saveLogEntry(screenshotFilename) {
  const dbPath = path.join(__dirname, '..', 'db.sqlite3');
  const db = new sqlite3.Database(dbPath);
  const id = uuid.v4();
  const timestamp = moment().format('YYYY-MM-DD HH:mm:ss');

  db.run(
    `INSERT INTO metatempo_log_record (identifier_uuid, screenshot_image_png, timestamp, is_sent_successfully)
     VALUES (?, ?, ?, ?)`,
    [id, screenshotFilename, timestamp, false],
    (err) => {
      if (err) console.error('Failed to save log entry:', err);
      else console.log('Log entry saved successfully.');
      db.close();
    }
  );
}

// Delete all log entries older than 30 days
function deleteOldLogs() {
  const dbPath = path.join(__dirname, '..', 'db.sqlite3');
  const db = new sqlite3.Database(dbPath);
  const cutoffDate = moment().subtract(parseInt(process.env.CLEAN_LOGS_OLDER_THAN_DAYS), 'days').format('YYYY-MM-DD HH:mm:ss');
  console.log("Cut-Off date has been determined as: ", cutoffDate);

  db.run(
    `DELETE FROM metatempo_log_record WHERE timestamp < ?`,
    [cutoffDate],
    (err) => {
      if (err) console.error('Failed to delete old log entries:', err);
      else console.log('All log entries older than ', cutoffDate, ' days are deleted.');
      db.close();
    }
  );
}

// Send unsent logs to the mainframe server
async function sendUnsentLogs() {
  const dbPath = path.join(__dirname, '..', 'db.sqlite3');
  const db = new sqlite3.Database(dbPath);

  deleteOldLogs(); // Clean up old logs

  db.all(`SELECT * FROM metatempo_log_record WHERE is_sent_successfully = 0`, async (err, rows) => {
    if (err) {
      console.error('Error retrieving unsent logs:', err);
      db.close();
      return;
    }

    const config = await getConfiguration();

    for (const row of rows) {
      try {
        const formData = new FormData();
        formData.append('metatempo_user_auth_key', config.user_auth_key);
        formData.append('metatempo_api_key', config.connection_api_key);

        // Construct the absolute path to the screenshot image
        const screenshotPath = path.join(mediaBasePath, row.screenshot_image_png.replace('metatempo/logs/', ''));

        if (!fs.existsSync(screenshotPath)) {
          console.error(`File not found for log ${row.identifier_uuid}: ${screenshotPath}`);
          continue;
        }

        formData.append('screenshot_image_png', fs.createReadStream(screenshotPath));
        formData.append(
          'snapshot_metadata',
          JSON.stringify({ timestamp: row.timestamp, identifier_uuid: row.identifier_uuid })
        );

        const response = await axios.post(`${SERVER_BASE_URL}/app/metatempo/tempo/screenshot/delivery/`, formData, {
          headers: {
            ...formData.getHeaders(),
          },
        });

        if (response.data.success) {
          // Update the log entry as sent successfully right after each successful send
          db.run(
            `UPDATE metatempo_log_record SET is_sent_successfully = 1 WHERE identifier_uuid = ?`,
            [row.identifier_uuid],
            (err) => {
              if (err) console.error('Failed to update log entry:', err);
              else console.log(`Log entry ${row.identifier_uuid} marked as sent successfully.`);
            }
          );
        } else {
          console.error(`Failed to send log ${row.identifier_uuid}:`, response.data.error);
        }
      } catch (error) {
        console.error(`Error sending log ${row.identifier_uuid}:`, error.message);
      }
    }
    db.close();
  });
}

// Start capturing screenshots
async function startTracking(config) {
  if (!isWithinTrackingTime(config)) {
    console.log('Tracking not active due to time or day restrictions.');
    return;
  }

  const interval = getIntervalSeconds(config.member_log_intervals) * 1000;
  console.log(`Starting tracking with interval: ${interval / 1000} seconds.`);

  screenshotJob = setInterval(() => {
    const screenshotFilename = `screenshot_${Date.now()}.png`;
    const screenshotPath = path.join(mediaBasePath, screenshotFilename);

    fs.mkdirSync(mediaBasePath, { recursive: true });

    screenshot({ filename: screenshotPath })
      .then(() => {
        console.log(`Captured screenshot at ${new Date()}`);
        saveLogEntry(screenshotFilename);
      })
      .catch((err) => {
        console.error('Failed to capture screenshot:', err);
      });
  }, interval);

  const sendLogsInterval = parseInt(process.env.LOG_SENDING_INTERVAL_MINUTES) * 60 * 1000;
  console.log('Tempo tracking started with sending interval: ', sendLogsInterval);
  sendLogsJob = setInterval(sendUnsentLogs, sendLogsInterval);
}

// Stop capturing screenshots
function stopTracking() {
  if (screenshotJob) {
    clearInterval(screenshotJob);
    screenshotJob = null;
    console.log('Tempo tracking stopped.');
  }
  if (sendLogsJob) {
    clearInterval(sendLogsJob);
    sendLogsJob = null;
    console.log('Stopped sending unsent logs.');
  }
}

// Toggle tracking on/off
async function toggleTracking(req, res) {
  try {
    isTrackingActive = !isTrackingActive;
    const config = await getConfiguration();

    if (!config) {
      console.error('Configuration not found in the database');
      res.writeHead(500, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: 'Configuration not found' }));
    }

    if (isTrackingActive) {
      await startTracking(config);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ status: 'Tracking started' }));
    } else {
      stopTracking();
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ status: 'Tracking stopped' }));
    }
  } catch (error) {
    console.error('Error in toggleTracking:', error);
    if (!res.headersSent) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'An error occurred while toggling tracking' }));
    }
  }
}

module.exports = {
  toggleTracking
};
