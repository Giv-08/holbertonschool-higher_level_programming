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
        i = 0
        while i < len(text):
            result += text[i]
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                if i + 1 < len(text) and text[i + 1] == ' ':
                    result += "\n\n"
                    while i + 1 < len(text) and text[i + 1] == ' ':
                        i += 1
                else:
                    result += "\n\n"
            i += 1
        print(result.strip())
    else:
        raise TypeError("text must be a string")
