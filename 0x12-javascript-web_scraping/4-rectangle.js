#!/usr/bin/node

module.exports = {
  Rectangle: function (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }

    this.print = function () {
      let addX = '';
      let x = 0;
      let y = 0;
      while (x < w) {
        addX = addX.concat('X');
        x++;
      }
      while (y < h) {
        console.log(addX);
        y++;
      }
    };

    this.rotate = function () {
      let hold = w;
      w = h;
      h = hold;
    };

    this.double = function () {
      w *= 2;
      h *= 2;
    };
  }
};
