#!/usr/bin/env python3
def uppercase(str):
    new = ''
    for alphabets in str:
        if 'a'<= alphabets <= 'z':
            new += chr(ord(alphabets) - 32)
        else:
          new += alphabets
    print(new)
