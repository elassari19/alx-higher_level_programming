#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// should select the file
const file = process.argv[2];
// should get text
const text = process.argv[3];
fs.writeFile(file, text, 'utf8', function (err, data) {
  // should read file as utf8
  if (err) {
    // should print error
    console.log(err);
  }
});
