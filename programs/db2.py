


import pymysql

#step1: connect to db
conn = pymysql.connect(host = "localhost",port=3306 , user='root',password='giri@123')
print(conn)

#step2
cursor = conn.cursor()
query = "insert into employees.empdb values('{}','{}')".format('public','phd')

#step3
cursor.execute(query)

#step4
print(cursor.rowcount,"row inserted")

conn.commit()
#step5
conn.close()


#string = "I love {} and {}"
#print(string.format("bang","hyd"))
#query = "insert into employees.empdb values('{}','{}')".format("public",'mtech')