# Birthday Json
import json
import os

def main():
    addNameBirth()
    
def addNameBirth():
    buffer_list = []
    with open('/PythonStuff/PracticePythonDotOrg/name_birth.json', 'r') as json_file:
        buffer_list = json.loads(json_file.read())

    print(buffer_list)    
    name_prompt = str(input('Enter a name for the dictionary: '))
    birth_prompt = str(input('Enter its birth date: '))
    buffer_list.append({name_prompt:birth_prompt})
    print(buffer_list)

    with open('/PythonStuff/PracticePythonDotOrg/name_birth.json', 'w') as json_file:
        json.dump(buffer_list, json_file, indent = 4)


if __name__ == '__main__':
    main()