#!/usr/bin/python3
"""
This module provides a class called MyInt inherited from int
the method MyInt behaves the opposite way during comparisons
"""

class MyInt(int):
    """
    This is a class called MyInt inherited from int
    """
    def MyInt(self):
        """
        the method MyInt behaves the opposite way during comparisons
        "==" is equal "!="

        Return: True is it's the opposite
        otherwise, False
        """
        if self == "==":
            return False
        elif self == "!=":
            return True
