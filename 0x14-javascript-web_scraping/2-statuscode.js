#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    console.log('code: ' + body);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
