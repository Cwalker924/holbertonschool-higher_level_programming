#!/usr/bin/python3
"""
This module holds only one function:
print_square()
"""


def print_square(size):
    typeError = ["size must be an integer", "size must be >= 0"]

    if isinstance(size, int) is False:
        raise TypeError(typeError[0])
    elif isinstance(size, float) is True and size < 0:
        raise TypeError(typeError[0])
    if size < 0:
        raise ValueError(typeError[1])

    for hash in range(size):
        print("#" * size)
