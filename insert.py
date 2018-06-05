# -*- coding: UTF-8 -*-
import sqlite3 as s
import time
import db_funcs as db
conn = s.connect("AttendanceSystem.db")
sql = "delete from start"
cur = conn.cursor()
cur.execute(sql)
conn.commit()
cur.close()
#format = "%Y/%m/%d/%H:%M:%S"
#date = time.strftime(format, time.localtime())
#db.inserdb_notcommute('1111', date)
#with s.connect("AttendanceSystem.db") as conn:

    #sql = "insert into emp(emp_id,emp_name,emp_age,emp_sex) values (?,?,?,?)"
    #sql = "insert into start(emp_id,date) values (?,?)"

    # 1건씩 추가하기
    # cur.execute(sql, ('정남진', 21, '경북 구미시1'))
    # cur.execute(sql, ('정남진', 21, '경북 구미시2'))

    # 리스트를 이용하여 자료 추가하기
    #infoList = [('3280','park','26','F'), ('1221','kim','49','M'), ('4747','kang','22','F')]
    # start 테이블

    #infoList = [('3280',date)]
    #cur.executemany(sql, infoList)
