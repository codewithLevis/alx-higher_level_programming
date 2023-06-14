#!/usr/bin/node

const [firstArgument] = process.argv.slice(2);
const parsedArg = parseInt(firstArgument);

// check if passed argument is an integer
if (isNaN(parsedArg)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${parsedNumber}`);
}
