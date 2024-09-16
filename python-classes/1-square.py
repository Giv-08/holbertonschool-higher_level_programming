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
        The area of the square calculated as side ** 2

    Methods
    -------
    __init__(size)
        initializes the square with a given side length
    area():
        Return the area of the square

    """
    def __init__(self, size=0):
        self.size = size
