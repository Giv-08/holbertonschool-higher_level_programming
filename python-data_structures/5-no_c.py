#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            # new_string = "".join(i for i in my_string if i not in my_string)
            new_string = my_string.translate({ord(i): None for i in 'cC'})
            # new_string += my_string
            return(new_string)
