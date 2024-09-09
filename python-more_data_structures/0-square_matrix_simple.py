#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(j * j)
        new.append(new_row)
    return new
