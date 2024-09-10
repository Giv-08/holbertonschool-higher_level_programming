#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_list = []
    for i in my_list:
        if i not in uni_list:
            uni_list.append(i)
    return sum(uni_list)
