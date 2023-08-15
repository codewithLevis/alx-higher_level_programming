#!/usr/bin/node

const files = process.argv.slice(2);
const fs = require('fs');
const file1 = fs.readFileSync(files[0], 'utf8');
const file2 = fs.readFileSync(files[1], 'utf8');
fs.writeFileSync(files[2], file1 + file2);
