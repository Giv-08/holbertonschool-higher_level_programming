#!/usr/bin/python3
"""
This module provides a class called BaseGeometry
"""


class BaseGeometry:
    """
    function that calculates area

    Parameters:
    self: the size

    Returns:
    None
    """
    def area(self):
        """
        function that calculates area

        Parameters:
        self: the size

        Returns:
        None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that calculates area

        Parameters:
        self: the size
        name: name must be string
        value: value must be integer

        Returns:
        None
        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
