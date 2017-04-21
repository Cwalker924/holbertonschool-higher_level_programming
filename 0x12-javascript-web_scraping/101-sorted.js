#!/usr/bin/node

let fileDict = require('./101-data').dict;

let myDict = {};
let i;
for (i in fileDict) {
  if (myDict[fileDict[i]]) {
    myDict[fileDict[i]].push(i);
  } else {
    myDict[fileDict[i]] = [];
    myDict[fileDict[i]].push(i);
  }
}
console.log(myDict);
