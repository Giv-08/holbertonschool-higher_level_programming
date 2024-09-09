#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        new = my_list[::-1]
        print("{:d}".format(new[i], end=""))
