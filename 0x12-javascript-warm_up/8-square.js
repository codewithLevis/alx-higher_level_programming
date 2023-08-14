#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) { console.log('Missing size'); } else if (size > 0) {
  for (let i = 0; i < size; i++) {
    let str = '';
    for (let j = 0; j < size; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
