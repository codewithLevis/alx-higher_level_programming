#!/usr/bin/node

const arr = process.argv.slice(2);

if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  let firstLargest = parseInt(arr[0]);
  let secondLargest = firstLargest;
  for (let j = 1; j < arr.length; j++) {
    if (parseInt(arr[j]) > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = parseInt(arr[j]);
    }
  }
  console.log(secondLargest);
}
