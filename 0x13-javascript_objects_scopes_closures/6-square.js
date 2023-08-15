#!/usr/bin/node

const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c) {
    c = typeof c === 'undefined' ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
