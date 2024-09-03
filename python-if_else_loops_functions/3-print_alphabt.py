#!/usr/bin/python3
for alphabets in range(97, 122 + 1):
    if alphabets not in (ord('e'), ord('q')):
        print("{}".format(chr(alphabets)), end='')
