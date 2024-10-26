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

const { app, BrowserWindow, screen } = require('electron');
const { exec } = require('child_process');
const axios = require('axios');
const path = require('path');

let mainWindow;
let floatingButton;

function checkServer() {
    return axios.get('http://127.0.0.1:8080')
        .then(() => true)
        .catch(() => false);
}

async function waitForServer() {
    let serverUp = false;
    while (!serverUp) {
        serverUp = await checkServer();
        if (!serverUp) await new Promise(resolve => setTimeout(resolve, 1000)); // Check every 1 second
    }
}

async function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1280,
        height: 800,
        resizable: true,
        webPreferences: {
            nodeIntegration: true,
        },
        icon: path.join(__dirname, 'assets/img/common/logo.png')
    });
    mainWindow.setAspectRatio(1280 / 800);
    await waitForServer();
    mainWindow.loadURL('http://127.0.0.1:8080');
}

async function createFloatingButton() {
  const { width, height } = screen.getPrimaryDisplay().workAreaSize;
  floatingButton = new BrowserWindow({
    width: 80,
    height: 80,
    x: width - 150,
    y: height - 100,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    resizable: false,
    hasShadow: true,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    }
  });

  await waitForServer();
  floatingButton.loadURL('http://127.0.0.1:8080/copilot/modal/');
  floatingButton.setIgnoreMouseEvents(false);
  if (process.platform === 'darwin') {
    floatingButton.setAlwaysOnTop(true, 'floating');
  }
}

app.whenReady().then(() => {
    exec("python3 manage.py runserver 8080", (err, stdout, stderr) => {
        if (err) {
            console.error(`Error starting Django server: ${err}`);
            return;
        }
        console.log("Django server started:", stdout);
    });

    createWindow();
    // createFloatingButton();
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
        // createFloatingButton();
    }
});
