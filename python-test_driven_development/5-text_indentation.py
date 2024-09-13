#!/usr/bin/python3
"""
This module provides a function print_square(size)
that print a square of '#'
size has to be an integer or float
TypeError is raised if size is not integer type.
"""


def text_indentation(text):
    """
    Prints a text with two lines after each of '.', '?' and ':'

    Parameters:
    text: must be string

    Returns:
    text: with no space at the beginning or at the end of each printed line

    Raises:
    TypeError: the text must be string type
    """
    if isinstance(text, str):
        result = ""
        for i in range(len(text)):
            result += text[i]
                # print("{}".format(text[i]), end="")
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                result += "\n"
        print(result.strip())
    else:
        raise TypeError("text must be a string")
