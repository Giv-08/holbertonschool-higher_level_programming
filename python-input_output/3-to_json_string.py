#!/usr/bin/python3
import json
"""This module handles a function
that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    '''
    This function returns the JSON representation
    of an object (string)

    Return: object(string)
    '''
    my_json = json.dumps(my_obj)
    print(my_json)
