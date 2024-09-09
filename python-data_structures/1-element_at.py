#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if i == idx:
            return ("{:d}".format(my_list[i]))
        elif i < 0 or i >= len(my_list):
            return None
    # for i, value in enumerate(my_list):
    #     if i == idx:
    #         return (value)
    #     elif i < 0 or i >= len(my_list):
    #         return None
