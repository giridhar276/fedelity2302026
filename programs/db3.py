


import pymysql
import csv
import os
try:
    #step1: connect to db
    conn = pymysql.connect(host = "localhost",port=3306 , user='root',password='giri@123')
    print(conn)
    #step2
    cursor = conn.cursor()
    count = 0
    filename = "employee.csv"
    # if the file is existing and the file size is greater than 0 the condition becomes true
    if os.path.isfile(filename) and os.path.getsize(filename)>0:
        with open(filename,"r") as fobj:
            header = fobj.readline()
            reader = csv.reader(fobj)
            for line in reader:
                workclass = line[1]
                education = line[3]
                query = "insert into employees.empdb values('{}','{}')".format(workclass,education)
                #step3
                cursor.execute(query)
                count = count + 1
        #step4
        print(count,"rows inserted")
        conn.commit()
        #step5
        conn.close()
    else:
        print("file is not found")
except Exception as err:
    print(err)