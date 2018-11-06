import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor();
sql = "create table test3(_id integer primary key autoincrement ,name varchar (20))"
cursor.execute(sql)
sql = "insert into test3(name) values('xiao')"
cursor.execute(sql)
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()
