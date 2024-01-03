#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// select url
const baseURL = process.argv[2];
const bodyResp = process.argv[3];
request(baseURL, (error, response, body) => {
  if (error == null) {
    // should write response body
    fs.writeFileSync(bodyResp, body);
  }
});
