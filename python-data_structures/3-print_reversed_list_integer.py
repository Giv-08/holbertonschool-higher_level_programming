#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        # my_list.reverse()
        new = my_list[::-1]
        # if isinstance(my_list[i], int):
        print("{:d}".format(new[i], end=""))
        # else:
        #     return
# while
# no reverse
