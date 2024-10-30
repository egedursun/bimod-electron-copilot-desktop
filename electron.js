/*
 * Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
 *
 * Project: Bimod.io™
 * File: electron.js
 * Last Modified: 2024-10-26 16:33:18
 * Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
 * Created: 2024-10-26 16:34:15
 *
 * This software is proprietary and confidential. Unauthorized copying,
 * distribution, modification, or use of this software, whether for
 * commercial, academic, or any other purpose, is strictly prohibited
 * without the prior express written permission of BMD™ Autonomous
 * Holdings.
 *
 *  For permission inquiries, please contact: admin@Bimod.io.
 */

const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const axios = require('axios');
const path = require('path');
const server = require('./electron_server/server');
const dotenv = require('dotenv');

// Determine the path to .env based on the environment
const isProduction = app.isPackaged; // Checks if the app is running in production

/*
const envPath = isProduction
  ? path.join(app.getAppPath(), 'Contents', 'Resources', '.env') // Production path
  : path.join(__dirname, '.env'); // Development path
 */

const envPath = path.join(__dirname, '.env'); // Development path

console.log("Attempting to load .env from:", envPath);
dotenv.config({ path: envPath });

// Debug logs to confirm loaded environment variables
console.log('BASE_PORT:', process.env.BASE_PORT);
console.log('BASE_URL:', process.env.BASE_URL);
console.log('DEFAULT_SCREEN_WIDTH:', process.env.DEFAULT_SCREEN_WIDTH);
console.log('DEFAULT_SCREEN_HEIGHT:', process.env.DEFAULT_SCREEN_HEIGHT);

let mainWindow;
let isRecording = false;

// Debugging logs to confirm paths and environment variables
console.log('App Path:', app.getAppPath());
console.log('BASE_PORT:', process.env.BASE_PORT);
console.log('BASE_URL:', process.env.BASE_URL);
console.log('DEFAULT_SCREEN_WIDTH:', process.env.DEFAULT_SCREEN_WIDTH);
console.log('DEFAULT_SCREEN_HEIGHT:', process.env.DEFAULT_SCREEN_HEIGHT);

// Construct the absolute path to manage.py
const managePyPath = path.join(app.getAppPath(), 'manage.py');

// Function to check if the server is running
function checkServer() {
    return axios.get(process.env.BASE_URL)
        .then(() => true)
        .catch(() => false);
}

// Wait until the server is up and running
async function waitForServer() {
    let serverUp = false;
    while (!serverUp) {
        serverUp = await checkServer();
        if (!serverUp) await new Promise(resolve => setTimeout(resolve, 1000)); // Check every 1 second
    }
}

// Function to create the main application window
async function createWindow() {
  mainWindow = new BrowserWindow({
    width: parseInt(process.env.DEFAULT_SCREEN_WIDTH || '800'), // Fallback to default if undefined
    height: parseInt(process.env.DEFAULT_SCREEN_HEIGHT || '600'), // Fallback to default if undefined
    resizable: true,
    webPreferences: {
      nodeIntegration: true,
    },
    icon: path.join(app.getAppPath(), 'src/assets/img/common/logo.icns') // Ensure correct icon format for macOS
  });

  // Set the aspect ratio based on width and height environment variables
  mainWindow.setAspectRatio(parseInt(process.env.DEFAULT_SCREEN_WIDTH) / parseInt(process.env.DEFAULT_SCREEN_HEIGHT));

  // Wait for the Django server to start and then load the main URL
  await waitForServer();
  mainWindow.loadURL(process.env.BASE_URL);
}

// Start the Django server and create the Electron window
app.whenReady().then(async () => {
    exec(`python3 ${managePyPath} runserver ${process.env.BASE_PORT || 55000}`, (err, stdout, stderr) => {
        if (err) {
            console.error(`Error starting Django server: ${err}`);
            return;
        }
        console.log('Django server started:', stdout);
    });

    // Create the main application window
    createWindow();
    server.start();
});

// Handle app lifecycle events
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
