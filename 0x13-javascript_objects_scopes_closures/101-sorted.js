#!/usr/bin/node

// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end
// shoulld computes a dictionary of user ids by occurrence

const dictionary = require('./101-data').dict;
const newdictionary = {};

for (const key in dictionary) {
  if (newdictionary[dictionary[key]] === undefined) {
    newdictionary[dictionary[key]] = [];
  }
  newdictionary[dictionary[key]].push(key);
}
console.log(newdictionary);
