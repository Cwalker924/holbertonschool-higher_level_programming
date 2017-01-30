#!/usr/bin/python3
"""
This module holds only one function:
say_my_name()
"""


def say_my_name(first_name, last_name=""):
    typeError = ["first_name must be a string", "last_name must be a string"]

    if isinstance(first_name, str) is False:
        raise TypeError(typeError[0])
    if isinstance(last_name, str) is False:
        raise TypeError(typeError[1])

    print("My name is {} {}".format(first_name, last_name), end="")
    print("")
