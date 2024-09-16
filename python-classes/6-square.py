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

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(' ' * self.position[0] + self.size * '#')
