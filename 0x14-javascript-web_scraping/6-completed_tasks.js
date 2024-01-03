#!/usr/bin/node
const request = require('request');

// select url
const baseURL = process.argv[2];
request(baseURL, (error, response, body) => {
  const tasks = {};
  if (error) {
    // should print error
    console.log(error);
  }
  // parse data
  const data = JSON.parse(body);
  data.forEach(element => {
    if (element.completed) {
      if (!tasks[element.userId]) {
        tasks[element.userId] = 0;
      }
      tasks[element.userId]++;
    }
  });
  console.log(tasks);
});
