#!/usr/bin/node

if (process.argv.length <= 2 || process.argv[2] === '1' ||
    process.argv[2] === '0') {
  console.log(0);
} else {
  let myList = [];
  let i = 3;
  while (i < process.argv.length) {
    myList.push(process.argv[i]);
    i++;
  }
  let a = myList.sort();
  console.log(a[a.length - 1]);
}
