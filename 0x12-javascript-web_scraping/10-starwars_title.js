#!/usr/bin/node

const request = require('request');
const episode = parseInt(process.argv[2]);
const url = 'http://swapi.co/api/films/' + episode;

request(url, (error, respose, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
