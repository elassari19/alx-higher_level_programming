#!/usr/bin/node

// Write a function that returns the number of occurrences in a list:
// Prototype: exports.nbOccurences = function (list, searchElement)
// should exports.nbOccurences

/**
 * @param {list} list - list
 * @param {number} searchElement - search Element
 * @returns {number} - number
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
