#!/usr/bin/python3
"""
Square class
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (isinstance(position[0], int) is not True or
                isinstance(position[1], int) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = position
        if (isinstance(position[0], int) is not True or
                isinstance(position[1], int) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        gap = " " * self.__position[0]
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(gap, "#" * self.__size))
