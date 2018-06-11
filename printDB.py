import sqlite3
str = 'AttendanceSystem'
db = sqlite3.connect(str+".db")
db.row_factory = sqlite3.Row
cur = db.cursor()
query = cur.execute("select * from "+"start" )
for row in query.fetchall():
   #print (row["emp_id"],row["uid"],row["name"])

   #print(row["emp_id"], row["emp_name"])
   print(row["emp_id"], row["date"])
   #year, month, day, h = row["date"].split('/')
   #print (year,month,day,h)
# while True:
#     student = cur.fetchone()
#     if not student: break
#     print (student)
cur.close()
db.close()
