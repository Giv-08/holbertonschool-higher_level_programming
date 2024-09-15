#!/usr/bin/python3
"""
This module provides a function say_my_name(first_name, last_name="")
that prints two strings.
If first_name and last_name have to be strings.
TypeError is raised if first_name or last_name are string type.
"""


# def say_my_name(first_name, last_name=""):
#     """
#     Prints first string and second string

#     Parameters:
#     first_name: string
#     last_name: string or default as empty string

#     Returns:
#     None

#     Raises:
#     TypeError: If first_name or last_name is not string
#     """
#     if not isinstance(first_name, str):
#         raise TypeError("first_name must be a string")
#     if not isinstance(last_name, str):
#         raise TypeError("last_name must be a string")

#     # print("My name is {} {}".format(first_name, last_name).strip())
#     print(f"My name is {first_name} {last_name}".strip())
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Arguments:
    first_name -- first name as a string
    last_name -- last name as a string, defaults to an empty string

    Raises:
    TypeError -- if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
