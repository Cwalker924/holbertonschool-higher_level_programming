#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for ch in my_dict:
        new_dict[ch] = my_dict[ch] * 2
    return(new_dict)
