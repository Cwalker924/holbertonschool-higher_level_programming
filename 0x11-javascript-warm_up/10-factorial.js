#!/usr/bin/node

num = parseInt(process.argv[2]);
function fact(a) {
    let i = 1;
    while (num >= 1) {
	i *= num;
	num--;
    }
    console.log(i);
}

if (num) {
    fact(num)
} else {
    console.log(1);
}
