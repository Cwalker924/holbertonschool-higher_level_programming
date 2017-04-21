#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const myList = list.map((x, y) => {
  return (x * y);
});
console.log(myList);
