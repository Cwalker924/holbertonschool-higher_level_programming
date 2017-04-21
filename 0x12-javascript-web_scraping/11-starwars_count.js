#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let x = 0;
    let count = 0;
    while (x < results.length) {
      let dicts = results[x];
      let characters = dicts['characters'];
      x++;
      let y = 0;
      while (y < characters.length) {
        if (characters[y].match(/18/)) {
          count += 1;
        }
        y++;
      }
    }
    console.log(count);
  }
});
