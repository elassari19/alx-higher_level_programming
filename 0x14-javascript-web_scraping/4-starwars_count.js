#!/usr/bin/node
const request = require('request');

// select api url
const URL = process.argv[2];
// request function
request(URL, (error, response, body) => {
  if (error) {
    // should print error
    console.log(error);
  } else if (body) {
    // should parse data
    const data = JSON.parse(body);
    // should filter data
    const movies = data.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    // should print length of movies
    console.log(movies.length);
  }
});
