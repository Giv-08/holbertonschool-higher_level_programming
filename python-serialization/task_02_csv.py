#!/usr/bin/python3
"""This module demonstrates in reading data from one
format (CSV) and converting it into another format (JSON)
using serialization techniques
"""
from csv import DictReader
# import csv
import json


def convert_csv_to_json(cvs_file):
    try:
        if cvs_file:
            with open('csv_file', 'r') as f:
                my_dict = DictReader(f)
                list_dict = list(my_dict)
            with open('data.json', 'w') as file:
                json.dumps(list_dict, file)
            return True
    except FileNotFoundError:
        return False
