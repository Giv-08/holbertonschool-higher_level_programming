#!/usr/bin/python3
"""
This module provides a function that returns
the list of sorted integers
"""


class MyList(list):
    """
    Prints the sorted list of integers

    Parameters:
    self: the list of integers

    Returns:
    a list of sorted integers
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
