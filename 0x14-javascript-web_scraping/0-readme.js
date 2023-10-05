const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
