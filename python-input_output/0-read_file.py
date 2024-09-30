#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""
import json

def read_file(filename=""):
    '''
    This function prints contents from the given file using "with"
    and open()
    The last line must skip the new line
    '''
    with open(filename, 'r') as file:
        text = file.read()
        for i, line in enumerate(text):
            if i < len(text) - 1:
                print(line, end="")
        print(text[-1].rstrip(), end="")
    # print(s)
        # lines = file.readlines()
        # length = len(lines)
        # if length == 1:
        #     print(lines[0].strip())
        # else:
        #     for i, line in enumerate(lines):
        #         if i < length - 1:
        #             print(line, end="")
        #     print(lines[-1].rstrip(), end="")
