## server.py
# -*- coding: UTF-8 -*-
from socket import *
import thread
import db_funcs
import time

# soket.soket()함수 인자는 두개이다
# 패밀리: 첫번째 인자는 패밀리이다. 소켓의 패밀리란,
# “택배상자에 쓰는 주소 체계가 어떻게 되어 있느나”에 관한 것으로 흔히 AF_INET, AF_INET6를 많이 쓴다.
# 전자는 IP4v에 후자는 IP6v에 사용된다. 각각 socket.AF_INET, socket.AF_INET6로 정의되어 있다.
# 두번째 인자는 타입: 소켓 타입이다. raw 소켓, 스트림소켓, 데이터그램 소켓등이 있는데,
# 보통 많이 쓰는 것은 socket.SOCK_STREAM 혹은 socket.SOCK_DGRAM이다.
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
def receive_msg():
    while True:
        global conn, format
        data = conn.recv(1024)
        print "data : " + data
        if data.find('$'):
            msg, emp_id = data.split('$')
        print (msg, emp_id)
        if not data:
            continue
        elif msg == "Add":
            if db_funcs.chkemp_id(emp_id):
                conn.send('AddOK'.encode())
            else:
                conn.send('AddNOTOK'.encode())
            print "등록메세지"
        elif msg == "cul":
            print "출근메세지"
            date = time.strftime(format, time.localtime())
            db_funcs.insertdb_commute(emp_id, date)


        elif msg == "notcul":
            print "퇴근메세지"
            db_funcs.inserdb_notcommute(emp_id, date)

        else:
            print"잘못된 값 입력"
          #인자 => 연결을 원하는 클라이언트가 대기할 수 있는 큐의 크기
thread.start_new_thread(c_accept,(),)
thread.start_new_thread(receive_msg,(),)

while True:
    pass
   # msg = conn.recv(1024)
    #if msg.find(';'):

    #uid,date = msg.split(';')
    #db.saveCommute(uid,date)
   # print('uid : ' + uid )

#print('msg from client: ' + msg)
#conn.send(msg.encode())
#print('msg to client: ' + msg)
conn.close()


# import 가 아니고 파이썬 인터프리터가 최초로 파일을 읽어서 실행하는 경우
# 파이썬 인터프리터는 소스파일을 읽고, 그 안의 모든 코드를 실행하게 되는데,
# 코드를 실행하기 전에 특정한 변수값을 정의하는데
# 그중 하나가 __name__ 이라는 변수를 __main__ 으로 세팅을 한다.
# 아래 소스는'만일 이 파일이 인터프리터에 의해서 실행되는 경우라면' 이라는 의미를 갖는다.
#즉 다른 import로 사용하지 않고 바로 실행하면 아래코드가 참이다
#if __name__ == '__main__':
 # run_server()
