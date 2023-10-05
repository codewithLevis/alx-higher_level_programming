const request = require('request');
const uri = process.argv[2];

request.get(uri, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    let movieCount = 0;

    for (const movie of data.results) {
      if (
        movie.characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/'
        )
      ) {
        movieCount++;
      }
    }
    console.log(movieCount);
  } else {
    console.error(err);
  }
});
