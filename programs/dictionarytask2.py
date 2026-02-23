

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}

print(type(employees))

for key,value in employees.items():
    print(value['name'].ljust(10), value['department'])


for empinfo in employees.values():
    print(empinfo['name'].ljust(10) , empinfo['department'])



