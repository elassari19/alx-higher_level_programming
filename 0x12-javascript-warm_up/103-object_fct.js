#!/usr/bin/node

/*
  Update this script by adding a new function incr that increments the integer value.
  You are not allowed to use var
  sould adding a new function incr that increments the integer value
*/

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = () => {
  myObject.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
