#!/usr/bin/python3
"""This module a function def pascal_triangle(n)
that returns a list of lists of integers representing
the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[]]
    triangle[0].append(1)
    for _ in range(1, n):
        row = []
        temp = [0] + triangle[-1] + [0]
        for j in range(len(triangle) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return(triangle)
