#!/usr/bin/node
const process = require('process');
const request = require('request');

// should get the url
const url = process.argv[2];
request(url, function (error, response) {
  if (error == null) {
    // should print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
