#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for i in reversed(roman_string):
        if roman_string.startswith('IX'):
            i += 9
        elif roman_string.startswith('X'):
            i += 10
        elif roman_string.startswith('V'):
            i += 5
        elif roman_string.startswith('I'):
            i += 1
        elif roman_string.startswith('L'):
            i += 50
        elif roman_string.startswith('C'):
            i += 100
        elif roman_string.startswith('D'):
            i += 500
        elif roman_string.startswith('M'):
            i += 1000
        return i
    # loop string in reversed
    # assign current to dict values[c] == key
    # if current less than prev
    # total - current
    # or
    # totle + current and prev equals current

    # values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # total = 0
    # prev = 0

    # for c in reversed(roman_string):
    #     current = values[c]
    #     if current < prev:
    #         total -= current
    #     else:
    #         total += current
    #         prev = current
    # return total
