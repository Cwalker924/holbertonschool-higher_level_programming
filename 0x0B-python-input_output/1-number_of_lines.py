#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, "r") as file:
        ln = 0
        for line in file:
            ln += 1
        return (ln)
