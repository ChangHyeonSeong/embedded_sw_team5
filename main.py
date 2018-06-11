#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtCore, QtGui
import face_recog
import Read
import AddFrame
import sqlite3
import socket
import face_recog
import thread
import time
HOST = '192.168.0.8' 
PORT = 8888
ADDR = (HOST,PORT)
#한글설정
QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))
class MainWindow(QtGui.QWidget):
    def bbb(self,str):
	self.label.setText(str)
############################메인화면 초기화 부분###############################
#전부 버튼을 비활성화 시키고 rfid카드를 인식한다. 등록 된 카드일 경우 출퇴근, 
#취소버튼을 활성화 시키고 그렇지 않은 경우 카드 등록, 취소 버튼을 활성화 시킨다.
    def reset(self):
	self.read_uid=''
	self.button.setEnabled(False)
	self.button2.setEnabled(False)
	self.button3.setEnabled(False)
	self.button4.setEnabled(False)
	time.sleep(2)
	self.read_uid = Read.run()
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(self.read_uid,))
	rows = cur.fetchall()
	conn.close()
	if not rows:
		self.button.setEnabled(True)
		self.button4.setEnabled(True)
		self.label.setText("등록 되지않은 카드입니다.")
	else:
		self.button4.setEnabled(True)
		self.button2.setEnabled(True)
		self.button3.setEnabled(True)
		self.label.setText("반갑습니다")
    def socket_init(self):
    	self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	try:
	    self.csocket.connect(ADDR)
	except  Exception as e:
	    print('error addr %s:%s',ADDR)
	    sys.exit()
	finally:
	    #sock.close()
	    print "dd"
################################# qt main 화면 ################################
    def __init__(self): 
	self.socket_init()
        QtGui.QWidget.__init__(self)
	self.label = QtGui.QLabel("카드를 인식 해주세요",self)
	self.label.setGeometry(10,10,200,20)
	
        self.setWindowTitle("Click Window")
        self.setGeometry(300, 200, 300, 200)
        self.button = QtGui.QPushButton('카드 등록', self)
        self.button.setGeometry(10, 40, 100, 30)
	self.button.setEnabled(False)
        self.button.clicked.connect(self.add)

        self.button2 = QtGui.QPushButton('출근', self)
        self.button2.setGeometry(10, 90, 100, 30)
	self.button2.setEnabled(False)
        self.button2.clicked.connect(self.cul)

        self.button3 = QtGui.QPushButton('퇴근', self)
        self.button3.setGeometry(10, 140, 100, 30)
	self.button3.setEnabled(False)
        self.button3.clicked.connect(self.notcul)

        self.button4 = QtGui.QPushButton('취소', self)
        self.button4.setGeometry(190, 140, 100, 30)
	self.button4.setEnabled(False)
        self.button4.clicked.connect(self.cancel)


        #QtCore.QObject.connect(self.button, QtCore.SIGNAL('clicked()'), self.hello)

#############################취소 버튼 클릭 이벤트###########################
    def cancel(self):
            self.label.setText("카드를 인식 해주세요")
	    thread.start_new_thread(mw.reset,(),)
########################카드 등록 버튼 클릭 이벤트###########################
    def add(self):
	    self.w = AddFrame.AddWindow(self.read_uid, self.csocket)
	    self.w.exec_()
	    self.label.setText("카드를 인식 해주세요")
	    thread.start_new_thread(mw.reset,(),)
#############################출근 버튼 클릭 이벤트###########################
    def cul(self):
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(self.read_uid,))
	rows = cur.fetchall()
	conn.close()
	emp_id =  str(rows[0][1])
	if face_recog.run(emp_id):
	    self.csocket.send(("cul$"+str(rows[0][1])).encode())
	    self.label.setText("카드를 인식 해주세요")
	else:
	    self.label.setText("다시 시도 해주세요")
	thread.start_new_thread(mw.reset,(),)
############################퇴근 버튼 클릭 이벤트###########################
    def notcul(self):
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(self.read_uid,))
	rows = cur.fetchall()
	conn.close()
	emp_id =  str(rows[0][1])
	if face_recog.run(emp_id):
	    self.csocket.send(("notcul$"+str(rows[0][1])).encode())
            self.label.setText("카드를 인식 해주세요")
	else:
            self.label.setText("다시 시도 해주세요")
	thread.start_new_thread(mw.reset,(),)

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    thread.start_new_thread(mw.reset,(),)
    sys.exit(app.exec_())

