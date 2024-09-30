#!/usr/bin/python3
"""This module handles a function that writes
an Object to a text file, using a JSON representation
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
with open('add_item.json', 'a') as file:
    list = args[1:]
    list.append()
    save_to_json_file(list, 'add_item.json')
    load_from_json_file('add_item.json')
