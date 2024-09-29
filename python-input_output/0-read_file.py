#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""

def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as op:
        for line in op:
            if line[:-1]:
                print(line.rstrip(), end="")
            else:
                print(line, end="")
