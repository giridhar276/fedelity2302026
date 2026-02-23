#p    y     t     h      o      n        p    r    o     g    r     a    m    m   i   n    g
# 0   1     2      3     4      5   6    7    8    9    10    11   12    13  14   15  16   17
#                                                                       -5   -4   -3  -2   -1  

name = "python programming"
print(name)
# slicing
#string[start:stop:step]
print("I love",name)
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
print(name[0:10])
print(name[8:10])
print(name[3:6])

print(name[0:18:1])
print(name[0:18])
print(name[0:18:2])
print(name[0:18:4])
print(name[-4:-2])

print(name[0:18:1])
print(name[0:18])
print(name[:]) # start = 0  , stop = 18 , step = 1
print(name[::])# start = 0  , stop = 18 , step = 1
print(name[::-1]) 
print(name[5::-1])
print(name[8:2:-1])




name = "python programming language"
print(name.capitalize())
print(name.upper())
print(name.isupper())

print(name.lower())   # displaying string in lower
print(name.islower()) # validating whether hte string is lower or not
print(name.count("p"))
print(name.count("z"))
print(name.endswith("g"))
print(name.startswith("p"))
print(name.startswith("z"))
print(name.split(" "))
print(name.find("ram")) # if existing it returns the starting index of substring
                        # if not existing .. it returns -1

aname = " python  "
print(len(aname))    # return the no. of characters
print(aname.strip()) # remove whitespaces at both ends
print(len(aname.strip()))
print(len(aname.lstrip())) # only remove at left side
print(len(aname.rstrip())) # only remove at right side

print(name.center(60))
print(name.encode("utf-8"))  # convertin the string to byte format # utf-8 is default
print(name.encode("utf-16"))
print(name.replace("python","java"))
bname = "python      programming"
print(bname.replace("      "," "))

########### string formatting ###########
string = "I love {} and {}"
print(string.format("Delhi","Hyderabad"))
print(string.format("python","java"))

age = 30
print(f"I am {age} years old")


# conditions
if 1 < 2 :
    print("true: 1 < 2")
    print("inside if")
    print("Still inside if ")


name = "python programming"
if name.islower():
    print("string is lower")


if name.startswith("p"):
    print("its python programming")

if name.endswith("g"):
    print("its someother language")


if 1 == 2:
    print("both are equals")


lang = input("Enter any langauge")
if lang == "python":
    print("its python")



############ if else ###########

if 1 < 2 :
    print("true: 1 < 2")
    print("inside if")
    print("Still inside if ")
else:
    print("false")

name = "python programming"
if name.islower():
    print("string is lower")
else:
    print("string is upper")


if name.startswith("p"):
    print("its python programming")
else:
    print("its somther langauge")


if 1 == 2:
    print("both are equal")
else:
    print("both are unequal")


# check whether the substring is existing or not
name = "python programming"
if "ram" in name:
    print("its python")


