# -*- coding: UTF-8 -*-
import sqlite3


#conn = sqlite3.connect('employee.db')
#conn = sqlite3.connect('start.db')
conn = sqlite3.connect('AttendanceSystem.db')
c = conn.cursor()

#c.execute("CREATE TABLE emp( emp_id TEXT PRIMARY KEY, emp_name TEXT, emp_age TEXT, emp_sex TEXT)")
#INTEGER PRIMARY KEY AUTOINCREMENT 자동증가
#c.execute("CREATE TABLE start( id INTEGER PRIMARY KEY AUTOINCREMENT,emp_id TEXT, date TEXT, CONSTRAINT fk_uid FOREIGN KEY(emp_id) REFERENCES emp(emp_id))")
c.execute("CREATE TABLE end( id INTEGER PRIMARY KEY AUTOINCREMENT, emp_id TEXT, date TEXT, CONSTRAINT fk_uid FOREIGN KEY(emp_id) REFERENCES emp(emp_id))")
#c.execute("drop table end")

conn.commit()
conn.close()
