import xml.etree.ElementTree as ET
import json


def element_to_dict(element):
    result = {'name': element.tag, 'attributes': {}}

    for name, value in element.attrib.items():
        result['attributes'][name] = value

    children = list(element)
    if children:
        result['children'] = [element_to_dict(child) for child in children]
    else:
        result['text'] = element.text.strip() if element.text else None

    return result


with open('schedule.xml', 'r') as file:
    root = ET.fromstring(file.read())

xml_dict = element_to_dict(root)

json_data = json.dumps(xml_dict, indent=4)

with open('schedule.json', 'w') as file:
    file.write(json_data)