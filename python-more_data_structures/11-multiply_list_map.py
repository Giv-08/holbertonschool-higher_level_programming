#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    for i in my_list:
        result = map(lambda i: i * number, my_list)
        return (list(result))
