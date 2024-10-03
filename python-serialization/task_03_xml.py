#!/usr/bin/python3
"""This module demonstrates serialization and
deserialization using XML as an alternative format to JSON
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom
import xml.dom.minidom


# def serialize_to_xml(dictionary, filename):
#     root = ET.Element("data")
#     for key, value in dictionary.items():
#         child = ET.SubElement(root, key)
#         child.text = str(value)

#     # tree = ET.ElementTree(root)
#     # xmlstr = ET.tostring(root, encoding='utf-8', method='xml')
#     # pretty_xml = minidom.parseString(xmlstr).toprettyxml(indent="    ")
#     # tree.write(filename, encoding='utf-8', xml_declaration=True)

#     # with open(filename, 'w') as file:
#     #     file.write(pretty_xml)

#     dom = xml.dom.minidom.parse(filename) # or xml.dom.minidom.parseString(xml_string)
#     pretty_xml_as_string = dom.toprettyxml()
def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode()

    dom = xml.dom.minidom.parseString(xmlstr)
    pretty_xml = dom.toprettyxml(indent="    ")

    with open(filename, 'w') as file:
        file.write(pretty_xml)

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
