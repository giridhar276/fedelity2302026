book  = {"chap1":10 ,"chap2":20 ,"chap3":30 }


#print(book["chap4"])
print(book.get("chap4")) # if key exists.. it returns value
                         # if key is not found...it returns None

# display dictionary
print(book)
# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)
# display individual values
print(book["chap1"]) #10
print(book["chap2"]) #20

## methods
# display all the keys
print( book.keys())

# display all the values
print(book.values())

# display key-value pairs
print(book.items())


book.pop("chap1") # chap1-10 will be removed from dictionary
print(book)
# will remove the last key-value pair
book.popitem()
book.popitem()
book.popitem()
print(book)

## combining 2 dictionaries
book  = {"chap1":10 ,"chap2":20 ,"chap3":30 }
newbook = {"chap4":40,"chap5":50}
#method1
book.update(newbook)
print(book)
# method2
finalbook = { **book, **newbook}
print(finalbook)

print("\n--- More Dictionary Methods ---\n")

# clear() - removes all items from dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print("Original person:", person)
person_copy = person.copy()  # create a copy first
person_copy.clear()
print("After clear():", person_copy)
print("Original person (unchanged):", person)

# copy() - creates a shallow copy
student = {"name": "Alice", "grade": "A", "marks": 95}
student_copy = student.copy()
student_copy["marks"] = 100  # modify the copy, original remains unchanged
print("\nOriginal student:", student)
print("Copied student (modified):", student_copy)

# fromkeys() - creates a new dictionary with specified keys and value
keys = ["a", "b", "c", "d"]
dict_from_keys = dict.fromkeys(keys, 0)
print("\nDictionary from keys:", dict_from_keys)

# setdefault() - returns value if key exists, else inserts key with default value
car = {"brand": "Toyota", "model": "Corolla"}
color = car.setdefault("color", "White")  # key doesn't exist, so adds it
print("\nCar after setdefault:", car)
brand = car.setdefault("brand", "Honda")  # key exists, so returns existing value
print("Brand value:", brand)

# check if key exists
fruits = {"apple": 5, "banana": 3, "orange": 2}
print("\nDictionary:", fruits)
if "apple" in fruits:
    print("'apple' exists in fruits")
if "grape" not in fruits:
    print("'grape' does not exist in fruits")

# len() - get number of items
print("\nNumber of items in fruits:", len(fruits))

# del - delete specific key-value pair
del fruits["banana"]
print("After del fruits['banana']:", fruits)

# iterate through dictionary
print("\nIterating through dictionary:")
numbers = {"one": 1, "two": 2, "three": 3}
for key in numbers:
    print(f"Key: {key}, Value: {numbers[key]}")

# iterate using items()
print("\nIterating with items():")
for key, value in numbers.items():
    print(f"Key: {key}, Value: {value}")

# iterate using keys()
print("\nIterating with keys():")
for key in numbers.keys():
    print(f"Key: {key}")

# iterate using values()
print("\nIterating with values():")
for value in numbers.values():
    print(f"Value: {value}")

# nested dictionary
company = {
    "name": "Tech Corp",
    "employees": {
        "emp1": {"name": "John", "salary": 50000},
        "emp2": {"name": "Jane", "salary": 60000}
    },
    "location": "NYC"
}
print("\nCompany name:", company["name"])
print("Employee 1 name:", company["employees"]["emp1"]["name"])
print("Employee 1 salary:", company["employees"]["emp1"]["salary"])