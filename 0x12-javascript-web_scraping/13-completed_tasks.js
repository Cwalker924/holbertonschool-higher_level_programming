#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  let myDict = {};
  let bodyText = JSON.parse(body);
  let i = 0;

  while (i < bodyText.length) {
    let user = bodyText[i].userId;
    if (user in myDict) {
      myDict[user] += 1;
    } else {
      myDict[user] = 1;
    }
  }
  console.log(myDict);
});
