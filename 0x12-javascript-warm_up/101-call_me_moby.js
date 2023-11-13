#!/usr/bin/node

/*
  Write a function that executes x times a function.
  The function must be visible from outside
  Prototype: function (x, theFunction)
  You are not allowed to use var
  sould executes x times a function
*/

export const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
