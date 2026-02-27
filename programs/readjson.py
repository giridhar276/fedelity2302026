

import json 
'''
with open('employee.json', 'r') as file:
    data = json.load(file)
    for key,value in data.items():
        print(key,value)
'''


with open('employee1.json', 'r') as file:
    data = json.load(file)
    for key,value in data.items():
        print(value['name'])


