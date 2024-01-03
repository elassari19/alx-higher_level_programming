#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films';

// first argument should be movie ID
const movieId = process.argv[2];
request(`${baseUrl}/${movieId}/`, (error, response, body) => {
  // should fetch data
  if (error) {
    // should print error
    console.log(error);
  }
  const data = JSON.parse(body);
  // should print response.title
  console.log(data.title);
});
