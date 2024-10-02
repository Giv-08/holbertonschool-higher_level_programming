#!/usr/bin/python3
"""This module demonstrates in reading data from one
format (CSV) and converting it into another format (JSON)
using serialization techniques
"""
from csv import DictReader
import json


# def convert_csv_to_json(cvs_file):
#     try:
#         if cvs_file:
#             with open('csv_file', 'r') as f:
#                 my_dict = DictReader(f)
#                 list_dict = list(my_dict)

#             with open('data.json', 'w') as file:
#                 json.dump(list_dict, file)
#             print("Conversion successful!")
#             return True
#         else:
#             print("No CSV file provided.")
#             False
#     except FileNotFoundError:
#         print(f"File not found: {csv_file}")
#         return False
#     except Exception as e:
#         print(f"An error occured: {e}")
#         return False
def convert_csv_to_json(csv_file):
    try:
        if csv_file:
            print(f"Attempting to open CSV file: {csv_file}")
            with open(csv_file, 'r') as f:
                my_dict = DictReader(f)
                list_dict = list(my_dict)

            with open('data.json', 'w') as file:
                json.dump(list_dict, file, indent=4)
            print("Conversion successful!")
            return True
        else:
            print("No CSV file provided.")
            return False
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
