#!/usr/bin/node

let num = parseInt(process.argv[2]);
function fact (a) {
  let i = 1;
  if (a === '0' || a === '1') {
    return (1);
  }
  while (num >= 1) {
    i *= num;
    num--;
  }
  console.log(i);
}

fact(num);
