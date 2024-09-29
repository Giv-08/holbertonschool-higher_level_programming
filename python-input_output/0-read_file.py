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
        for line in op:
            if line[:-1]:
                print(line.rstrip(), end="")
            else:
                print(line, end="")
