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
      while (x < w) {
        addX = addX.concat('X');
        x++;
      }
      let y = 0;
      while (y < h) {
        console.log(addX);
        y++;
      }
    };
  }
};
