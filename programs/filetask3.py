


import csv
try:
    mcount = 0
    fcount = 0
    with open("employee.csv","r") as fobj:
        header = fobj.readline()
        reader = csv.reader(fobj)
        for line in reader:
            gender = line[9].strip()
            if gender == "Male":
                mcount+=1
            if gender == "Female":
                fcount+=1

        print("Total male count:",mcount)
        print("Total female count:",fcount)
except Exception as err:
    print("file not found.. please check")
    print("system error:",err)