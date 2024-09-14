#!/usr/bin/python3
"""
This module provides a function print_square(size)
that print a square of '#'
size has to be an integer or float
TypeError is raised if size is not integer type.
"""


def matrix_divided(matrix, div):
    """
    Prints divides all elements of a matrix

    Parameters:
    matrix (list of lists of numbers): The 2D matrix to be processed.
    div (number): The divisor. Must be non-zero.

    Returns:
    list of lists of floats: The new matrix with each element divided by div.

    Raises:
    TypeError: the matrix must be string or float type
    ZeroDivisionError: can't be divided by 0
    """
    # if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix != matrix:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    i = 0
    for i in matrix:
        new_matrix.append([round(j / div, 2) for j in i])
    return new_matrix
