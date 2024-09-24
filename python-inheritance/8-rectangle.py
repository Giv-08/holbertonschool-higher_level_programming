#!/usr/bin/python3
"""
This module provides a class called BaseGeometry and a subclass Rectangle
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        function that calculates area

        Parameters:
        self: the size

        Raises:
            Exception: Indicating that the area() method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that calculates area

        Parameters:
        self: the size
        name: name must be string
        value: value must be integer

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class Rectangle inherited from class Geometry
    """
    def __init__(self, width, height):
        """
        function that instantiates a rectangle instance

        Parameters:
        self: the size
        width: mustr be integer
        height: must be integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
        # if not isinstance(self.__width, int):
        #     raise super().integer_validator("width", width)
        # if not isinstance(self.__height, int):
        #     raise super().integer_validator("height", height)
        # if self.__width < 0:
        #     raise super().integer_validator("width", width)
        # if self.__height < 0:
        #     raise super().integer_validator("height", height)
