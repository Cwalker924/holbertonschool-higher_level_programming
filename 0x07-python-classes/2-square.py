#!/usr/bin/python3
"""
Square class
"""


class Square:
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is not True:
            raise TypeError("size mist be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
