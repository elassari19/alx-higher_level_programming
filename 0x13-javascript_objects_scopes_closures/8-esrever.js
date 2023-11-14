#!/usr/bin/node

// Write a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
// You are not allow to use the built-in method reverse
// should returns the reversed version

/**
 * @param {list} list - list
 * @returns {number} - number
 */
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
