#!/usr/bin/python3
"""
This module holds only one function:
add_integer()
"""

def add_integer(a, b):
    if isinstance(a, int) == False and isinstance(a, float) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) == False and isinstance(b, float) == False:
        raise TypeError("b must be an integer")
    """
    uncomment for Reminder key:
    print(isinstance(a, int), end=" ==> ")
    print("'isinstance(a, int)'")
    print(type(a), end=" ==> ")
    print("'type(a)'")
    print(type(int(a)), end=" ==> ")
    print("'type(int(a))'")

    """
    return(int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod("tests/0-add_integer.txt")
