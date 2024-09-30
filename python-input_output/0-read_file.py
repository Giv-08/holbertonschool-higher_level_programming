#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""


def read_file(filename=""):
    '''
    This function prints contents from the given file using "with"
    and open()
    The last line must skip the new line
    '''
    with open(filename, 'r', encoding="utf-8") as op:
        lines = op.readlines()
        op = len(lines)
        if op == 1:
            print(lines)
        for i, line in enumerate(lines):
            if i < op - 1:
                print(line, end="")
        print(lines[-1].rstrip(), end="")
