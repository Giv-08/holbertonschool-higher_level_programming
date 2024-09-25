#!/usr/bin/python3
"""
This module provides a function that sets an attribute
to an object
"""


def add_attribute(self, attr, value):
    """
    Set an attribute on the instance.

    Parameters:
    attr (str): The name of the attribute to set.
    value: The value to assign to the attribute.

    Raises:
    TypeError: If the attribute cannot be set.
    """
    if not hasattr(self, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)
