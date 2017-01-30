#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for ch in set_1:
        if ch in set_2:
            new_list.append(ch)
    return(new_list)
