# -*- coding: UTF-8 -*-
import sqlite3 as s
import time


#insert 실행함수 , with문 -> try catch문을 대체함 자동으로 디비 커넥션을 닫아줌
#def insertData(table,uid,date):
#    with s.connect(table + ".db") as conn:
#        cur = conn.cursor()
#
#       sql = "insert into " + table + "(uid,date) values (?,?)"
#
#       # 리스트를 이용하여 자료 추가하기 리스트안에 여러개의 튜플을 넣어 복수의 데이터 삽입가능
#       # infoList = [('179133227217','3393','성창현'), ('16910619073','3384','남현준'), ('32102169137','3374','박도현')]
#       infoList = [(uid,date)]
#       cur.executemany(sql, infoList)
#
#       conn.commit()
#       cur.close()

#클라이언트에게 받은 데이터를 출근,퇴근인지 구분 하고 디비에 저장
#def saveCommute(uid,date):
#    isStart = False
#    db = s.connect("start.db")
##    db.row_factory = s.Row
#    cur = db.cursor()
##    query = cur.execute("select * from start")
#    for row in query.fetchall():
#        if row["uid"] == uid:
#            if row["date"][0:10] == date[0:10]:
#                isStart = True
#                print('출근하였음: ' + row["date"])
#    cur.close()
#    db.close()#
#
#    if isStart:
#        insertData('end', uid, date)
#    else:
#       insertData('start', emp_id, date)
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








