import sqlite3

conn = sqlite3.connect('cul.db')
c = conn.cursor()
c.execute("CREATE TABLE emp_list ( uid INT PRIMARY KEY, emp_id INT)")
conn.commit()
conn.close()
