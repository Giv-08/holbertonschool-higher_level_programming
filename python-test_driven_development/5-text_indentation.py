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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = {'.', '?', ':'}
    result = []
    i = 0
    while i < (len(text)):
        result.append(text[i])
        if text[i] in char:
            result.append("\n\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    result = "".join(result).rstrip()
    print(result[:-3], end="")
