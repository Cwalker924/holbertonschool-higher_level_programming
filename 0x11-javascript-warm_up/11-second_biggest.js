#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let myList = [];
  let i = 2;
  while (i < process.argv.length) {
    myList.push(process.argv[i]);
    i++;
  }
  let a = myList.sort();
  console.log(a[a.length - 2]);
}
