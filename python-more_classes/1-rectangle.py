#!/usr/bin/python3
"""This module handles a rectangle area calculation.
This module provides a function calculate_rectangle()
that calculates the area of rectangle by using the length of one side
"""


class Rectangle:
    """A class represents a rectangle.
    Attributes
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.

    Methods
    -------
    __init__(width=0, height=0):
        initializes the rectangle with a given side length
    area():
        Return the area of the rectangle

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.heigth = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
