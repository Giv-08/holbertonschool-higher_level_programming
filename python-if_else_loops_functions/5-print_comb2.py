#!/usr/bin/python3
for num in range(100):
    if num in range(0, 10):
        print("0{}, ".format(num), end='')
    elif num in range(10, 99):
        print("{}, ".format(num), end='')
print(99)
