#!/usr/bin/node

const [arg1] = process.argv.slice(2);
const squareSize = parseInt(arg1);

if (isNaN(squareSize)) {
  console.log("Missing size");
} else {
  if (squareSize <= 0) {
    console.log("Invalid size");
  } else {
    for (let i = 0; i < squareSize; i++) {
      let line = "";
      for (let j = 0; j < squareSize; j++) {
        line += "X";
      }
      console.log(line);
    }
  }
}