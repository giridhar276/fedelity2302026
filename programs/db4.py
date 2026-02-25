


import pymysql
from openpyxl import Workbook
import time 
#step1: connect to db
conn = pymysql.connect(host = "localhost",port=3306 , user='root',password='giri@123')
print(conn)
wb = Workbook()
# grab the active worksheet
ws = wb.active

#step2
cursor = conn.cursor()
query = "select * from employees.empdb" # select * from database.tablename

#step3
cursor.execute(query)

#step4
for record in cursor.fetchall():
    #print(record)
    ws.append(record)

filename = time.strftime("empinfo_%d_%b_%Y.xlsx")
wb.save(filename)
#step5
conn.close()