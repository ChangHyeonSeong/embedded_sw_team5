# -*- coding: UTF-8 -*-
import sqlite3 as s
import time

def insertdb_commute(emp_id, date):
    year, month, day, h2 = date.split('/')
    conn = s.connect('AttendanceSystem.db')
    conn.row_factory = s.Row
    cur = conn.cursor()
    query = cur.execute("select * from start where emp_id = " + emp_id)
    for row in query.fetchall():
        year2, month2, day2, h2 = row["date"].split('/')
        if month == month2 and day == day2:
            print "이미출근했음"
            conn.close()
            return False
    cur.execute("INSERT INTO start(emp_id, date) VALUES(?, ?)", (emp_id, date))
    conn.commit()
    conn.close()
    return True
def inserdb_notcommute(emp_id, date):
    year, month, day, h2 = date.split('/')
    conn = s.connect('AttendanceSystem.db')
    conn.row_factory = s.Row
    cur = conn.cursor()
    query = cur.execute("select * from start where emp_id = " + emp_id)
    rows = query.fetchall()
    if not rows:
        print "해당 사원번호는 출근한 내용이 없습니다."
        conn.close()
        return False
    query = cur.execute("select * from end where emp_id = " + emp_id)
    rows = query.fetchall()
    for row in rows:
        year2, month2, day2, h2 = row["date"].split('/')
        if month == month2 and day == day2:
            print "이미퇴근했음"
            conn.close()
            return False
    cur.execute("INSERT INTO end(emp_id, date) VALUES(?, ?)", (emp_id, date))
    conn.commit()
    conn.close()
    return True
def chkemp_id(emp_id):
    conn = s.connect("AttendanceSystem.db")
    cur = conn.cursor()
    cur.execute("select * from emp where emp_id = ?", (emp_id,))
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    if rows:
        return True
    else:
        return False








