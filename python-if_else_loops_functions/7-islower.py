#!/usr/bin/python3
def islower(c):
    if not isinstance(c, str):
        print("Traceback (most recent call last):")
        return None
    elif c.islower():
        return True
    else:
        return False
