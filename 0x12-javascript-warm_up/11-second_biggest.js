#!/usr/bin/node

/*
  Write a script that searches the second biggest integer in the list of arguments.
  You can assume all arguments can be converted to integer
  If no argument passed, print 0
  If the number of arguments is 1, print 0
  You must use console.log(...) to print all output
  You are not allowed to use var
  sould searches the second biggest integer
*/

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const listIntagers = process.argv.sort().reverse();
  console.log(listIntagers[1]);
}
