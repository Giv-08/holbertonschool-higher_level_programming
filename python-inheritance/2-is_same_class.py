#!/usr/bin/python3
"""
This module provides a function that returns True
if the object is exactly an instance of the specified class
otherwise, False
"""


def is_same_class(obj, a_class):
    """
    Custom list class that can print itself sorted.

    Parameters:
    self: the list of integers

    Returns:
    None
    """
    if (type(obj) is a_class):
        return True
    else:
        return False
