
import pymysql

#step1: connect to db
conn = pymysql.connect(host = "localhost",port=3306 , user='root',password='giri@123')
print(conn)

#step2
cursor = conn.cursor()
query = "select * from employees.empdb" # select * from database.tablename

#step3
cursor.execute(query)

#step4
for record in cursor.fetchall():
    print(record)

#step5
conn.close()