#!/usr/bin/python3
"""This module writes a script adds all
arguments to a Python list, and then save them to a file:
"""
import os
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open('add_item.json', 'a') as file:
    if os.path.exists('add_item.json'):
        lst = load_from_json_file
    else:
        lst = []
    lst.extend(sys.argv[1:])
    save_to_json_file(lst, 'add_item.json')
    # load_from_json_file('add_item.json')
