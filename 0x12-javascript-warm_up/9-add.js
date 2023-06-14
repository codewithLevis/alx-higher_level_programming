#!/usr/bin/node

function add(a, b){
  return a + b;
};

const [firstArg, secondArg] = process.argv.slice(2);
const num1 = parseInt(firstArg);
const num2 = parseInt(secondArg);

if (isNaN(num1) || isNaN(num2)) {
  console.log("Invalid arguments");
} else {
  const result = add(num1, num2);
  console.log(result);
}