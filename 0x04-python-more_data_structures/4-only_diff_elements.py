#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    u_set = []
    for ch in set_1:
        if ch not in set_2:
            u_set.append(ch)
    for ch in set_2:
        if ch not in set_1:
            u_set.append(ch)
    return(u_set)
