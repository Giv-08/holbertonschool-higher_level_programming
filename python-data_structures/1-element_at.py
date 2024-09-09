#!/usr/bin/python3
def element_at(my_list, idx):
    for i, value in enumerate(my_list):
        if i == idx:
            return (value)
        elif i < 0 or i >= len(my_list):
            return None
