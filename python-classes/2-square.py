#!/usr/bin/python3
"""This module handles a square area calculation.
This module provides a function calculate_square()
that calculates the area of square by using the length of one side
"""


class Square:
    """A class represents a square.
    Attributes
    ----------
    size : int
        The length of one side of the square.
    area : int
        The area of the square calculated as side * side

    Methods
    -------
    __init__(size)
        initializes the square with a given side length
    calculate_area():
        Return the area of the square

    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
