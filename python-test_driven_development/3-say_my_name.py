#!/usr/bin/python3
"""
This module contains one function for printing a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints out the name.

    Args:
        first_name (string) : the first name
        last_name (string) : the last name

    Returns:
        Nothing.
    """

    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))
