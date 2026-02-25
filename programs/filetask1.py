

'''
write a program to read employee.csv and display workclass and education columns ONLY.


'''

import csv
try:
    with open("employee.csv","r") as fobj:
        header = fobj.readline()
        reader = csv.reader(fobj)
        for line in reader:
            print(line[1])
            print(line[3])
            print("-------------------")
except Exception as err:
    print("file not found.. please check")
    print("system error:",err)



open("employee.csv","r")