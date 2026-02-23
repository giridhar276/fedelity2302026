
students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]


for student in students:
    print("Student:",student['name'])
    print("Math:",student['marks']['math'])
    print("Science:",student['marks']['science'])
    print("-------------------------")


alist = [10,20,30]
for value in alist:
    print(value)