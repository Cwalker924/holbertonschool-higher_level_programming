#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):
    with open(filename, "r") as file:
        if (nb_lines <= 0):
            print(file.read(), end="")
        else:
            ln = 1
            for line in file:
                if (ln <= nb_lines):
                    print(line, end="")
                    ln += 1
