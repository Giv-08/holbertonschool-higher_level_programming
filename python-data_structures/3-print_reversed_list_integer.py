#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        my_list.reverse()
        if isinstance(i, int):
            print("{:d}".format(my_list[i], end=""))
        else:
            return
