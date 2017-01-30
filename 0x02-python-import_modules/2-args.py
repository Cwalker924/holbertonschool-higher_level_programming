#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args <= 0:
        delim = "."
        print("{:d} argument{:s}".format(args, delim))
    else:
        delim = ":"
        if args <= 1:
            print("{:d} argument{:s}".format(args, delim))
        else:
            print("{:d} arguments{:s}".format(args, delim))
        for i in range(1, len(sys.argv)):
            print("{:d}{:s} {:s}".format(i, delim, sys.argv[i]))
