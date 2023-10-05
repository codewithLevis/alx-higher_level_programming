#!/usr/bin/node

const request = require('request');
const uri = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(uri, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(err);
  }
});
