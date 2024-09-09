#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    for i in range(0, len(my_list)):
        if i < len(my_list):
            print("{:d}".format(my_list[i]), end="\n")
