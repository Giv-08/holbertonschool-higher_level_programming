#!/usr/bin/python3
"""
This module provides a class called MyInt inherited from int
the method MyInt behaves the opposite way during comparisons
"""


class MyInt(int):
    """
    This is a class called MyInt inherited from int
    """
    def __eq__(self, num):
        """
        the method __eq__ behaves the opposite way during comparisons
        "==" is equal "!="

        Return: True if it's the opposite
        """
        return not super().__eq__(num)

    def __ne__(self, num):
        """
        the method __ne__ behaves the opposite way during comparisons
        "==" is equal "!="

        Return: False if it's the opposite
        """
        return super().__eq__(num)
