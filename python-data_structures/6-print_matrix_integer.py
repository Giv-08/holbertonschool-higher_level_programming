#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        new = " ".join(map(str, matrix[i]))
        print("{}".format(new), end="\n")
