const fs = require('fs');
const path = require('path');
const axios = require('axios');
const FormData = require('form-data');
const sqlite3 = require('sqlite3').verbose();
const recorder = require('node-record-lpcm16');
require('dotenv').config();

let isRecording = false;
let recordingInstance;
let audioBuffer = [];
let errorOccurred = false;

function getApiKeyFromDatabase() {
    return new Promise((resolve, reject) => {
        const dbPath = path.join(__dirname, '..', 'db.sqlite3');
        const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READONLY, (err) => {
            if (err) {
                errorOccurred = true;
                return reject(err);
            }
        });

        db.get(`SELECT board_connection_api_key FROM meta_kanban_board_connection ORDER BY created_at DESC LIMIT 1`, (err, row) => {
            if (err) {
                errorOccurred = true;
                reject(err);
            } else {
                resolve(row ? row.board_connection_api_key : null);
            }
            db.close();
        });
    });
}

async function uploadRecording() {
    if (errorOccurred) {
        console.error('Error detected; skipping upload.');
        errorOccurred = false;  // Reset for next recording
        return;
    }

    try {
        const apiKey = await getApiKeyFromDatabase();
        if (!apiKey) {
            console.error('API key not found in the database');
            errorOccurred = true;
            return;
        }

        // Combine all audio chunks into a single buffer
        const audioData = Buffer.concat(audioBuffer);

        const url = `${process.env.SERVER_BASE_URL}/app/metakanban/meeting/recording/delivery/`;
        const formData = new FormData();
        formData.append('metakanban_api_key', `Bearer ${apiKey}`);
        formData.append('meeting_recording_audio_wav', audioData, {
            filename: 'recording.wav',
            contentType: 'audio/wav'
        });

        const response = await axios.post(url, formData, {
            headers: {
                ...formData.getHeaders(),
            }
        });

        console.log('Recording uploaded successfully:', response.data);
    } catch (error) {
        console.error('Error uploading recording:', error.response?.data || error.message);
        errorOccurred = true;
    } finally {
        // Clear the audio buffer after upload
        audioBuffer = [];
    }
}

function startRecording() {
    errorOccurred = false;  // Reset error flag for new recording

    recordingInstance = recorder.record({
        sampleRate: 16000,
        channels: 1,
        format: 'wav'
    });

    // Collect audio data into memory buffer
    recordingInstance.stream().on('data', (data) => {
        audioBuffer.push(data);  // Store each chunk in the array
        console.log('Recording audio data:', data.length);
    });

    recordingInstance.stream().on('error', (err) => {
        console.error('Error in audio stream:', err);
        errorOccurred = true;
        stopRecording();
    });

    recordingInstance.stream().on('close', () => {
        console.log('Recording stopped and ready for upload');
        uploadRecording();  // Upload after recording stops
    });

    console.log('Recording started and buffering in memory');
}

function stopRecording() {
    if (recordingInstance) {
        recordingInstance.stop();
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

    // Send response based on error status
    const responseMessage = errorOccurred
        ? { status: "Error occurred during recording process" }
        : { status: isRecording ? "Recording started" : "Recording stopped" };

    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(responseMessage));
}

module.exports = {
    handleToggleRecording
};
