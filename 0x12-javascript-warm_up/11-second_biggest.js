#!/usr/bin/node

let arr = process.argv.slice(2);

if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  arr = process.argv.slice(2).map((num) => parseInt(num));
  arr.sort(function (a, b) {
    return b - a;
  });
  const maxNum = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < maxNum) {
      console.log(arr[i]);
      process.exit(0);
    }
  }
}
