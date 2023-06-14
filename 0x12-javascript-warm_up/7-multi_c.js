#!/usr/bin/node

const [number] = process.argv.slice(2);
const parsedNumber = parseInt(number);

if (NaN(parsedNumber)) {
  console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < parsedNumber + 1; i++) {
      console.log("C is fun");
    }
}