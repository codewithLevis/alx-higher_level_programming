#!/usr/bin/node

const dict = require('./101-data').dict;

const arr = {};
for (const key in dict) {
  if (dict[key] in arr) {
    arr[dict[key]].push(key);
  } else {
    arr[dict[key]] = [key];
  }
}

console.log(arr);
