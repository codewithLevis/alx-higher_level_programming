#!/usr/bin/node

const num = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return n;
  }
  return n * factorial(n - 1);
}

const result = factorial(num);
console.log(result || 1);
