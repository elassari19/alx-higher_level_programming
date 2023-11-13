#!/usr/bin/node

/*
  Write a script that prints the first argument passed to it:
  If no arguments are passed to the script, print “No argument”
  You must use console.log(...) to print all output
  You are not allowed to use var
  You are not allowed to use length
  sould print print the first argument
*/

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
