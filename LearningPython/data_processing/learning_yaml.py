# YAML Ain't Makeup Language
# data serialization language
# used for configuration files, but also for data exchange

# YAML Python parser -> PyYAML
# allows to load, parse, write YAML

import yaml
import json

# YAML parser returns a regular Python object that best fits the data.
# In this case dictionary
# yaml.safe_load() parse all kinds of valid YAML strings
with open('/PythonStuff/LearningPython/data_processing/config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service)
print(prime_service['prime_numbers'])
print(prime_service['rest']['url'])

# Parsing files with multiple YAML documents
# YAML allows you to define multiple documents in one file, separating them with a triple dash (---)
# safe_load_all()

with open('/PythonStuff/LearningPython/data_processing/multi_doc.yml', 'r') as file:
    docs = yaml.safe_load_all(file)
    for doc in docs:
        print(doc)

# Writing (or dumping) YAML to a file
    # Create an initial configuration file with current settings for your user
    # To save state of your program in an easy to read file (instead of using something like Pickle)

name_yaml = """ 
- 'eric'
- 'justin'
- 'mary-kate'
"""

names = yaml.safe_load(name_yaml)

with open('/PythonStuff/LearningPython/data_processing/names.yml', 'w') as file:
    yaml.dump(names, file)

print(open('/PythonStuff/LearningPython/data_processing/names.yml').read())

# Converting YAML to JSON
with open('/PythonStuff/LearningPython/data_processing/config.yml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('/PythonStuff/LearningPython/data_processing/config.json', 'w') as json_file:
    json.dump(configuration, json_file)