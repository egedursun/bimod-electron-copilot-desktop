/*
 * Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
 *
 * Project: Bimod.io™
 * File: voice_recording.js
 * Last Modified: 2024-10-26 20:39:20
 * Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
 * Created: 2024-10-26 20:39:21
 *
 * This software is proprietary and confidential. Unauthorized copying,
 * distribution, modification, or use of this software, whether for
 * commercial, academic, or any other purpose, is strictly prohibited
 * without the prior express written permission of BMD™ Autonomous
 * Holdings.
 *
 *  For permission inquiries, please contact: admin@Bimod.io.
 */


const fs = require('fs');
const path = require('path');
const mic = require('mic');

let micInstance;
let isRecording = false;
let recordingStream;

function startRecording() {
    const recordingFilePath = path.join(require('electron').app.getPath('desktop'), `recording_${Date.now()}.wav`);

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
