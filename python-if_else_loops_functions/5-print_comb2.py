#!/usr/bin/python3
for num in range(100):
    if num < 99:
        print("{:02d}".format(num), end=', ')
    elif num == 99:
        print("{}".format(num), end='\n')
