#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if a != 0 and b != 0:
            result = a / b
            return result
        else:
            return None
    except ValueError:
        print()
    finally:
        print("Inside result: {}".format(result or None))
