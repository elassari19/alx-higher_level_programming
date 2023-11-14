#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of 5-square.js:
// You must use the class notation for defining your class and extends
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
// should create an instance method called charPrint(c)

const square = require('./5-square');
class Square extends square {
  /**
   * @property {method} charPrint - print
   * @returns console.log the size
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
