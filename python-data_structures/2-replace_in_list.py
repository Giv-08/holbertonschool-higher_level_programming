#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(0, len(my_list)):
        if i == idx:
            my_list.remove(my_list[i])
            my_list.insert(i, element)
            return (my_list)
        elif i < 0 or i >= len(my_list):
            return my_list
