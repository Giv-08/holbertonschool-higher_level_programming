#!/usr/bin/python3
"""
This module provides a function that returns
the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Prints the list of available attributes and methods of an object

    Parameters:
    obj: a class passed in parameter

    Returns:
    a list object

    """
    return dir(obj)
