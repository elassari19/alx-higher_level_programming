#!/usr/bin/node

// Write a function that converts a number from base 10 to another base passed as argument:
// Prototype: exports.converter = function (base)
// You are not allowed to import any file
// You are not allowed to declare any new variable (var, let, etc..)
// should converts a number from base 10 to another base

/**
 * @param {number} base - number
 * @returns {any} - base
 */
exports.converter = function (base) {
  function converted (number) {
    return number.toString(base);
  }
  return converted;
};
