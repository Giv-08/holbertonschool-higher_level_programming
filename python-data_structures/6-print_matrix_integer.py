#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        # new = " ".join(map(str, matrix[i]))
        # print("{:d}".format(new), end="\n")
        print(" ".join("{:d}".format(element) for element in i))
