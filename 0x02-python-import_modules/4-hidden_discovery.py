#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    length = len(dir(hidden_4))
    for i in range(0, length):
        if dir(hidden_4)[i][:2] != "__":
            print(dir(hidden_4)[i])
