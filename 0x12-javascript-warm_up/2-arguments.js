#!/usr/bin/node

/*
  Write a script that prints a message depending of the number of arguments passed:
  If no arguments are passed to the script, print “No argument”
  If only one argument is passed to the script, print “Argument found”
  Otherwise, print “Arguments found”
  You must use console.log(...) to print all output
  You are not allowed to use var
  sould print a message
*/

const message = process.argv.length === 2

  ? 'No argument' : process.argv.length === 3

    ? 'Argument found'

    : 'Arguments found';

console.log(message);
