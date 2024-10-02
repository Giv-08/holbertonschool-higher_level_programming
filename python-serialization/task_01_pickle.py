#!/usr/bin/python3
"""This module handles class called CustomObject
"""
import json
# import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        data = {
            'name': self.name,
            'age': self.age,
            'is_student': self.is_student
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return cls(data['name'], data['age'], data['is_student'])
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None
