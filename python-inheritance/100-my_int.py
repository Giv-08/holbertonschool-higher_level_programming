#!/usr/bin/python3
"""
This module provides a class called MyInt inherited from int
the method MyInt behaves the opposite way during comparisons
"""


class MyInt(int):
    """
    This is a class called MyInt inherited from int
    """
    # def __eq__(self, num):
    #     """
    #     the method __eq__ behaves the opposite way during comparisons
    #     "==" is equal "!="

    #     Return: True if it's the opposite
    #     """
    #     return super().__eq__(num) == False

    def __ne__(self, num):
        """
        the method __nq__ behaves the opposite way during comparisons
        "==" is equal "!="

        Return: False if it's the opposite
        """
        # return super().__eq__(num) == True
        if self == num:
            return False
        elif self and num == 0:
            return False
        else:
            return True
