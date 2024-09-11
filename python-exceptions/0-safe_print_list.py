#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        for i in range(x):
            print(my_list[i], end="")
            length += 1
        print()
        return length
    except IndexError:
            print("Error")
            return length
    # try:
    #     count = 0
    #     for i in range(x):
    #         print(my_list[i], end="")
    #         count += 1
    #     print()
    #     return count
    # except IndexError:
    #     print()
    #     return count
