#!/usr/bin/python3
"""This module writes a script adds all
arguments to a Python list, and then save them to a file:
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'
# with open('add_item.json', 'a') as file:
try:
    lst = load_from_json_file(file)
except FileNotFoundError:
    lst = []
lst.extend(sys.argv[1:])
load_from_json_file('add_item.json')
save_to_json_file(lst, 'add_item.json')
