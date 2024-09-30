#!/usr/bin/python3
"""This module writes a script adds all
arguments to a Python list, and then save them to a file:
"""
# import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
with open('add_item.json', 'a') as file:
    # list = []
    list.append(args[1:])
    save_to_json_file(list, 'add_item.json')
    load_from_json_file('add_item.json')
