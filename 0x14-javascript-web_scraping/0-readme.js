#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// should select the file
const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  // should read file as utf8
  if (err) {
    // should print error
    console.log(err);
  } else {
    // should write content of file
    process.stdout.write(data);
  }
});
