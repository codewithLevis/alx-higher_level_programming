#!/usr/bin/node

const request = require('request');

request.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response) => {
    if (!err && response.statusCode === 200) {
      const data = JSON.parse(response.body);

      for (const url of data.characters) {
        request.get(url, (error, response2) => {
          if (!error && response2.statusCode === 200) {
            const star = JSON.parse(response2.body);
            console.log(star.name);
          } else {
            console.error(error);
          }
        });
      }
    } else {
      console.error(err);
    }
  }
);
