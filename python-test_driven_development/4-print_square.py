#!/usr/bin/python3
"""
This module provides a function print_square(size)
that print a square of '#'
size has to be an integer or float
TypeError is raised if size is not integer type.
"""


def print_square(size):
    """
    Prints square of #

    Parameters:
    size: dimension of thesquare

    Returns:
    size: length of the square

    Raises:
    TypeError: the size must be an integer and not less than 0
    """
    if isinstance(size, int):
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
        if size < 0:
            raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be an integer")
