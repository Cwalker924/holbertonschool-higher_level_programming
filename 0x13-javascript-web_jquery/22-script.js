#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films?format=json';

request(url, (error, body) => {
  if (error) {
    return (error);
  }

  let results = JSON.parse(body).results;
  let i = 0;
  while (i < results.length) {
    $('UL#list_movies').append(results[i].title);
    i++;
  }
});
