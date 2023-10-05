const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, (error) => {
      console.log(error);
    });
  } else {
    console.log(err);
  }
});
