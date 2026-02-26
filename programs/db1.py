
import pymysql
import os
#pip install python-dotenv
from dotenv import load_dotenv
# we are loading all envrionment variables
load_dotenv()
hostname = os.getenv("HOST")
user = os.getenv("USER")
port = int(os.getenv("PORT"))
password = os.getenv("PASSWORD")

#step1: connect to db
conn = pymysql.connect(host = hostname,port=port , user=user,password=password)
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