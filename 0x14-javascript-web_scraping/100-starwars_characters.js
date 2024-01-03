#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_err, _res, body) {
  // parse data
  const data = JSON.parse(body).data;
  for (let i = 0; i < data.length; ++i) {
    // fetch data
    request(data[i], function (charerror, cahrresp, charbody) {
      console.log(JSON.parse(charbody).name);
    });
  }
});
