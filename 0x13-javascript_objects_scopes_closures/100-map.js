#!/usr/bin/node

const list = require('./100-data').list;

const arr = list.map((element, index) => {
  return element * index;
});

console.log(list);
console.log(arr);
