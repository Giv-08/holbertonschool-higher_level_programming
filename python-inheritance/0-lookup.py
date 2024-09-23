#!/usr/bin/python3
"""
This module provides a function that returns
the list of available attributes and methods of an object
TypeError is raised if size is not integer type.
"""

def lookup(obj):
    """
    Prints the list of available attributes and methods of an object

    Parameters:
    obj: a class passed in parameter

    Returns:
    a list object

    Raises:
    TypeError: the matrix must be string or float type
    ZeroDivisionError: can't be divided by 0
    ValueError: If the rows of the matrix are not all the same size
    """
    return dir(obj)
