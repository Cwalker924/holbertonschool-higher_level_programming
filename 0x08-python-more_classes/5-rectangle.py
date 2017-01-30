#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        self.height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width or self.__height == 0:
            self.__perimeter = 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Credit: Jennie Chu
        "https://github.com/JennieChu/holbertonschool-higher_level_programming/
        blob/master/0x08-python-more_classes/4-rectangle.py"
        """
        ln = ""
        if self.__width == 0 or self.__height == 0:
            return (ln)
            for h in range(self.__height):
                for w in range(self.__width):
                    ln += "#"
                ln += "\n"
            ln = ln[:-1]
            return (ln)

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return ("Rectangle(" +width+ ", " +height+ ")")

    def __del__(self):
        print("Bye rectangle...")
