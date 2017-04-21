#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/people/5/?format=json';

request(url, (error, body) => {
  if (error) {
    return (error);
  }

  let name = JSON.parse(body)['name'];
  $('DIV#character').html(name);
});
