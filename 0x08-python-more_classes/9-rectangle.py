#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return (Rectangle(size, size))

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
                ln += str(self.print_symbol)
            ln += "\n"
        ln = ln[:-1]
        return (ln)

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return ("Rectangle(" +width+ ", " +height+ ")")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
