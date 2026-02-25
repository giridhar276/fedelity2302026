


'''
write a program to read employee.csv and display workclass and education columns ONLY.


'''

import csv
try:
    workset = set()
    with open("employee.csv","r") as fobj:
        header = fobj.readline()
        reader = csv.reader(fobj)
        for line in reader:
            workclass= line[1]
            workset.add(workclass)
        for work in workset:
            print(work)
except Exception as err:
    print("file not found.. please check")
    print("system error:",err)
###################################################################
import csv
try:
    workdict = dict()
    with open("employee.csv","r") as fobj:
        header = fobj.readline()
        reader = csv.reader(fobj)
        for line in reader:
            workclass= line[1]
            workdict[workclass] = 1    #{"public":1, "private":1}
           
        for work in workdict:
            print(work)
except Exception as err:
    print("file not found.. please check")
    print("system error:",err)