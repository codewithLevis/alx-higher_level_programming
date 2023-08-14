#!/usr/bin/node

const add = function (number, theFunction) {
  number++;
  theFunction(number);
};

module.exports = { addMeMaybe: add };
