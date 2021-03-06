#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

        Rectangle.__init__(self, size, size)

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
