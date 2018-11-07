import mysql.connector

conn = mysql.connector.connect(user="root",password="admin",database="szt")
cursor = conn.cursor()
sql = "select * from tes7"
cursor.execute(sql)
values = cursor.fetchall()
print(values)
sql = "update set name = 'xiaoming' where _id = ?"
cursor.execute(sql,)
cursor.close()
conn.close
