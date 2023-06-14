#!/usr/bin/node

function factorial(number) {
  // check if the argument is an integer
  if (isNaN(number)) {
    return 1;
  }

  if (number === 0) {
    return 1;
  }

  return number * factorial(number - 1); // recursively calls the function
}

const [arg1] = process.argv.slice(2);
const num = parseInt(arg1);

const result = factorial(num);
console.log(result);
