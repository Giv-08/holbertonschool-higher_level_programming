#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except:
        print("{} is not an integer".format(value))
        # return value
