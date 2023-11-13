#!/usr/bin/node

/*
  Write a script that prints the addition of 2 integers
  The first argument is the first integer
  The second argument is the second integer
  You have to define a function with this prototype: function add(a, b)
  You must use console.log(...) to print all output
  You are not allowed to use var
  sould prints the addition of 2 integers
*/

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  }

  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
