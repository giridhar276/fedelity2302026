# method1
with open("employees.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

# method2
with open("employees.txt","r") as fobj:
    print(fobj.readlines())  
["ram,30,hyderabad","rita,25,bangalore"]

# method3
with open("employees.txt","r") as fobj:
    print(fobj.read())  # fobj.read() ------> string

# method4 - using csv library
import csv
with open("employees.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)

#method5: using pandas librrary
import pandas
print(pandas.read_csv("employees.txt", header = None))


