#!/usr/bin/node

// Write a function that prints the number of arguments already printed and the new argument value. (see example below)
// Prototype: exports.logMe = function (item)
// Output format: <number arguments already printed>: <current argument value>
// should prints the number of arguments

/**
 * @param {item} str - item
 * @returns console.log str
 */
let narg = 0;
exports.logMe = function (item) {
  console.log(`${narg}: ${item}`);
  narg++;
};
