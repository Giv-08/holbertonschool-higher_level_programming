#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = list(a_dictionary.keys())
    my_list.sort()
    sorted_dict = {i : a_dictionary[i] for i in my_list}
    for a, b in sorted_dict.items():
        print("{}: {}".format(a, b))
