#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return(None)
    sum = 0
    my_list = set(my_list)
    for num in my_list:
            sum += num
    return(sum)
