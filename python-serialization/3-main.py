#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

    # Debug output to compare loaded and original data
    print("\nComparing Loaded Data with Sample Dictionary:")
    print("Loaded Data:", deserialized_data)
    print("Sample Dictionary:", sample_dict)

    # Assert to check if the data matches
    assert deserialized_data == {key: str(value) for key, value in sample_dict.items()}, "Data loaded does not match data saved"

if __name__ == "__main__":
    main()
