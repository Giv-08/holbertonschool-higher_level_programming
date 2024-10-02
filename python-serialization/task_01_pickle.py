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
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Is Student: {self.__is_student}")

    def serialize(self, filename):
        data = {
            'name': self.__name,
            'age': self.__age,
            'is_student': self.__is_student
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
