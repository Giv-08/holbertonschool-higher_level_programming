#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    i = 0
    for i in range(len(argv)):
        if argv[i] == 0:
            print("{} argument.".format(i), end="\n")
        if argv[i] > 0:
            print("{} arguments:".format(i), end="\n")
            print("{}: {}".format(i, argv[i]), end="\n")
        i = i + 1
