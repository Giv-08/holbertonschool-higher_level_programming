#!/usr/bin/python3
"""
This module provides a function say_my_name(first_name, last_name="")
that prints two strings.
If first_name and last_name have to be strings.
TypeError is raised if first_name or last_name are string type.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first string and second string

    Parameters:
    first_name: string
    last_name: string or default as empty string

    Returns:
    str: first name and last name

    Raises:
    TypeError: If first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} 1}".format(first_name, last_name))
