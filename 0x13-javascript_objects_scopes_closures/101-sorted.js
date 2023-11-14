#!/usr/bin/node

// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end
// shoulld computes a dictionary of user ids by occurrence

const dictionary = require('./101-data').dict;

let new_dictionary_list = {'1': [], '2': [] , '3': []};
const len = Object.getOwnPropertyNames(dictionary).length

for (let i = 1; i< len; i++) {
  for (const property in dictionary) {
    if (i == dictionary[property]) {
      new_dictionary_list = {
        ...new_dictionary_list,
        [i]: [...new_dictionary_list[`${i}`], property]
      }
    }
  }
}

console.log(new_dictionary_list);
