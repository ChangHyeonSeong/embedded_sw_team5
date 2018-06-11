## server.py
# -*- coding: UTF-8 -*-
from socket import *
import thread
import db_funcs
import time


HOST = ''
PORT = 8888
ADDR = (HOST,PORT)
print('Server run !')
ssock = socket(AF_INET, SOCK_STREAM)
ssock.bind(ADDR)
ssock.listen(1)
conn, addr = ssock.accept()
format = "%Y/%m/%d/%H:%M:%S"

def c_accept():
    while True:
        global conn,addr
        ssock.listen(3)
        print ("waiting for con1nection")
        conn, addr = ssock.accept()
        print (addr)
#클라이언트로부터 카드등록이나 출퇴근 메시지를 받으면 그에 맞는 일을 처리하는 부분
def receive_msg():
    while True:
        global conn, format
        data = conn.recv(1024)
        if data.find('$'):
            msg, emp_id = data.split('$')
        print (msg, emp_id)
        if not data:
            continue
#클라이언트로부터 사원번호를 받으면 서버내 데이터베이스에서 직원테이블에 존재한지검사하여
#다시 클라이언트로 메세지를 보냄
        elif msg == "Add":
            print "등록메세지"
            if db_funcs.chkemp_id(emp_id):
                conn.send('AddOK'.encode())
            else:
                conn.send('AddNOTOK'.encode())
        elif msg == "cul":
#클라이언트에서 출근메세지와 사원번호를 받으면 해당 사원이 이미 출근 여부를 확인하고 저장
            print "출근메세지"
            date = time.strftime(format, time.localtime())
            db_funcs.insertdb_commute(emp_id, date)
#클라이언트에서 퇴근메세지와 사원번호를 받으면 해당 사원이 이미 퇴근 여부를 확인하고 저장
        elif msg == "notcul":
            print "퇴근메세지"
            date = time.strftime(format, time.localtime())
            db_funcs.inserdb_notcommute(emp_id, date)
        else:
            print"잘못된 값 입력"
thread.start_new_thread(c_accept,(),)
thread.start_new_thread(receive_msg,(),)

while True:
    pass
conn.close()
