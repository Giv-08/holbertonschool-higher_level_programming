#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""


def read_file(filename=""):
    '''
    This function prints contents from the given file using "with"
    and open()
    The last line must skip the new line
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()
        # length = len(lines)
        # if length == 1:
        #     print(lines[0].strip())
        # else:
        #     for i, line in enumerate(lines):
        #         if i < length - 1:
        #             print(line, end="")
        #     print(lines[-1].rstrip(), end="")
        for line in lines[:-1]:
            print(line, end="")
        if lines:
            print(lines[-1].rstrip(), end="")
