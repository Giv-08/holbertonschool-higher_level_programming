#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""


# def read_file(filename=""):
#     '''
#     This function prints contents from the given file using "with"
#     and open()
#     The last line must skip the new line
#     '''
#     with open(filename, 'r', encoding="utf-8") as op:
#         lines = op.readlines()
#         length = len(lines)
#         if length == 1:
#             print(lines[0].strip())
#         else:
#             for i, line in enumerate(lines):
#                 if i < length - 1:
#                     print(line, end="")
#             print(lines[-1].rstrip(), end="")
def read_file(filename=""):
    '''
    This function prints contents from the given file using "with" and open().
    The last line must skip the new line.
    '''
    with open(filename, 'r', encoding="utf-8") as op:
        lines = op.readlines()
        length = len(lines)
        if length == 1:
            # Single line, strip the newline at the end
            print(lines[0].strip())
        else:
            # Print all but the last line as is
            for i, line in enumerate(lines):
                if i < length - 1:
                    print(line, end="")
            # Print the last line without an additional newline
            print(lines[-1].rstrip(), end="")
