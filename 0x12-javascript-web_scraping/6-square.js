#!/usr/bin/node

const Square = require('./5-square.js').Square;

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    this.print();
  } else {
    let addC = '';
      let x = 0;
    while (x < this.size) {
	addC = addC.concat(c);
      x++;
    }
    let y = 0;
    while (y < this.size) {
      console.log(addC);
      y++;
    }
      console.log(addC);
  }
};

module.exports = {Square};
//module.Square = Square;
