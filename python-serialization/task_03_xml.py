#!/usr/bin/python3
"""This module demonstrates serialization and
deserialization using XML as an alternative format to JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    return ET.ElementTree(root).write(filename)

def convert_type(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for element in root:
        key = element.tag
        value = convert_type(element.text)
        new_dict[key] = value
    return new_dict
