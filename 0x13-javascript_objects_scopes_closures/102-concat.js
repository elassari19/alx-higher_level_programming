#!/usr/bin/node

// Write a script that concats 2 files.
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination
// should concats two files

const fs = require('fs');
const a = process.argv[2];
const b = process.argv[3];
const c = process.argv[4];

const dataA = fs.readFileSync(a, { encoding: 'utf8' });
const dataB = fs.readFileSync(b, { encoding: 'utf8' });
fs.writeFileSync(c, dataA + dataB, { encoding: 'utf8' });
