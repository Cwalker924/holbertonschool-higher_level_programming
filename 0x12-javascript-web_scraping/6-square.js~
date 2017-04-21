#!/usr/bin/node

module.exports = {
  Square: function (size) {
    if (size > 0) {
      this.size = size;
    }

    this.print = function () {
      let addX = '';
      let x = 0;
      let y = 0;
      while (x < size) {
        addX = addX.concat('X');
        x++;
      }
      while (y < size) {
        console.log(addX);
        y++;
      }
    };

    this.double = function () {
      size *= 2;
    };
  }
};
