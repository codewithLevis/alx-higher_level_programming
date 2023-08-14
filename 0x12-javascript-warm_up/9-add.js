#!/usr/bin/node

function add (a, b) { console.log(a + b); }

const [a, b] = process.argv.slice(2);

add(parseInt(a), parseInt(b));
