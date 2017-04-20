#!/usr/bin/node

let num = parseInt(process.argv[2]);
function fact (a) {
  let i = 1;
  if (a === '0' || isNaN(a)) {
    console.log(1);
  } else {
    while (num >= 1) {
      i *= num;
      num--;
    }
    console.log(i);
  }
}

fact(num);
