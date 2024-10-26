const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const axios = require('axios');
const path = require('path');

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
    const win = new BrowserWindow({
        width: 1280,
        height: 800,
        resizable: true,
        webPreferences: {
            nodeIntegration: true,
        },
        icon: path.join(__dirname, 'assets/img/common/logo.png')
    });

    win.setAspectRatio(1280 / 800);

    await waitForServer();
    win.loadURL('http://127.0.0.1:8080');
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
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
});
