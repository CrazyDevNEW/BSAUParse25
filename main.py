import xml.etree.ElementTree as ET
import json


def element_to_dict(element):
    # Имя и атрибуты элемента
    result = {'name': element.tag, 'attributes': {}}

    for name, value in element.attrib.items():
        print(name, value)
        result['attributes'][name] = value

    # Дочерние элементы
    children = list(element)
    if children:
        result['children'] = [element_to_dict(child) for child in children]
    else:
        result['text'] = element.text.strip() if element.text else None

    return result


# Чтение schedule.xml
root = ET.parse("schedule.xml").getroot()

# Создание словаря для корневого элемента
xml_dict = element_to_dict(root)

# Сериализация словаря в JSON
json_data = json.dumps(xml_dict, indent=4)

# Запись JSON-данных в файл
with open('schedule.json', 'w') as file:
    file.write(json_data)