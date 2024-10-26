/*
 * Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
 *
 * Project: Bimod.io™
 * File: server.js
 * Last Modified: 2024-10-26 20:37:50
 * Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
 * Created: 2024-10-26 20:37:51
 *
 * This software is proprietary and confidential. Unauthorized copying,
 * distribution, modification, or use of this software, whether for
 * commercial, academic, or any other purpose, is strictly prohibited
 * without the prior express written permission of BMD™ Autonomous
 * Holdings.
 *
 *  For permission inquiries, please contact: admin@Bimod.io.
 */


const http = require('http');

//############################################################################################################
//############################################################################################################
// HANDLERS
//############################################################################################################
const voiceRecording = require('./voice_recording');
//############################################################################################################
//############################################################################################################

const server = http.createServer((req, res) => {
    // Set CORS headers
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:8080');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    // Handle preflight requests (CORS pre-checks for POST requests)
    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }
    //############################################################################################################
    //############################################################################################################
    // ROUTES
    //############################################################################################################
    if (req.url.startsWith('/toggle-recording')) {
        voiceRecording.handleToggleRecording(req, res);
    } else {
        res.writeHead(404);
        res.end();
    }
    //############################################################################################################
    //############################################################################################################
});

module.exports = {
    start: () => {
        server.listen(9090, () => {
            console.log('Electron internal server running on http://localhost:9090');
        });
    }
};
