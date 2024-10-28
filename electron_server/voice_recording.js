const fs = require('fs');
const path = require('path');
const mic = require('mic');
const axios = require('axios');
const FormData = require('form-data');
const sqlite3 = require('sqlite3').verbose();
require('dotenv').config();

let micInstance;
let isRecording = false;
let recordingStream;
let recordingFilePath;

function startRecording() {
    recordingFilePath = path.join(require('electron').app.getPath('desktop'), `recording_${Date.now()}.wav`);

    micInstance = mic({
        rate: '16000',
        channels: '1',
        debug: true,
        fileType: 'wav'
    });

    recordingStream = micInstance.getAudioStream();
    recordingStream.pipe(fs.createWriteStream(recordingFilePath));

    recordingStream.on('data', (data) => {
        console.log('Recording audio data:', data.length);
    });

    recordingStream.on('error', (err) => {
        console.error('Error in audio stream:', err);
    });

    recordingStream.on('close', () => {
        console.log('Recording stopped and file saved');
        uploadRecording(); // Call upload function once recording stops
    });

    micInstance.start();
    console.log('Recording started:', recordingFilePath);
}

function stopRecording() {
    if (micInstance) {
        micInstance.stop();
        console.log('Recording stopped');
    }
}

function getApiKeyFromDatabase() {
    return new Promise((resolve, reject) => {
        const dbPath = path.join(__dirname, '..', 'db.sqlite3');
        const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READONLY, (err) => {
            if (err) {
                return reject(err);
            }
        });

        db.get(`SELECT board_connection_api_key FROM meta_kanban_board_connection ORDER BY created_at DESC LIMIT 1`, (err, row) => {
            if (err) {
                reject(err);
            } else {
                resolve(row ? row.board_connection_api_key : null);
            }
            db.close();
        });
    });
}

async function uploadRecording() {
    try {
        const apiKey = await getApiKeyFromDatabase();
        if (!apiKey) {
            console.error('API key not found in the database');
            return;
        }

        const url = `${process.env.SERVER_BASE_URL}/app/metakanban/meeting/recording/delivery/`;
        const formData = new FormData();

        // Match the field names exactly as required by Django view
        formData.append('metakanban_api_key', `Bearer ${apiKey}`);
        formData.append('meeting_recording_audio_wav', fs.createReadStream(recordingFilePath));

        const response = await axios.post(url, formData, {
            headers: {
                ...formData.getHeaders(),
            }
        });

        console.log('Recording uploaded successfully:', response.data);
    } catch (error) {
        console.error('Error uploading recording:', error.response?.data || error.message);
    } finally {
        // Clean up by deleting the recording file after upload
        fs.unlink(recordingFilePath, (err) => {
            if (err) console.error('Failed to delete recording file:', err);
            else console.log('Recording file deleted after upload');
        });
    }
}

function handleToggleRecording(req, res) {
    isRecording = !isRecording;
    if (isRecording) {
        startRecording();
    } else {
        stopRecording();
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: isRecording ? "Recording started" : "Recording stopped" }));
}

module.exports = {
    handleToggleRecording
};
