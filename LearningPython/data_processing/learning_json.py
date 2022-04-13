# JavaScript Object Notation
# Language independent data format
# JSON's library you can read, write, and parse JSON

import json

# Parsing a string or decoding
# json.loads()

# it converts:
    # objects to dictionaries
    # arrys to lists
    # booleans, integers, floats, strings are recognized and propertly converted
    # null to None

with open('/PythonStuff/LearningPython/data_processing/json.txt','r') as f:
    person = json.loads(f.read())

# json.dumps() convert a python object consisting of dict, lists, and other native types into string
person_dump = json.dumps(person, indent=2)

print(type(person['name']), type(person['age']), type(person['married']))
print(person_dump)

# How to read a JSON file
with open('/PythonStuff/LearningPython/data_processing/data.json') as json_file:
    data = json.load(json_file)
print(data)    

data['name'] = 'john'
# How to write JSON to a file in Python
with open('/PythonStuff/LearningPython/data_processing/data.json', 'w') as json_file:
    json.dump(data, json_file)
