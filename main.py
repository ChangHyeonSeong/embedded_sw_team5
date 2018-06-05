#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtCore, QtGui
import face_recog
import Read
import AddFrame
import sqlite3
import socket
HOST = '192.168.0.8' 
PORT = 8888
ADDR = (HOST,PORT)
class MainWindow(QtGui.QWidget):
    def socket_init(self):
    	self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	try:
	    self.csocket.connect(ADDR)
	except  Exception as e:
	    print('error addr %s:%s'%self.ADDR)
	    sys.exit()
	finally:
	    #sock.close()
	    print "dd"

    def __init__(self):
	self.socket_init()
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Click Window")
        self.setGeometry(300, 200, 300, 200)
        self.button = QtGui.QPushButton('add', self)
        self.button.setGeometry(10, 30, 100, 30)
        self.button.clicked.connect(self.add)

        self.button2 = QtGui.QPushButton('cul', self)
        self.button2.setGeometry(10, 80, 100, 30)
        self.button2.clicked.connect(self.cul)

        self.button3 = QtGui.QPushButton('not cul', self)
        self.button3.setGeometry(10, 130, 100, 30)
        self.button3.clicked.connect(self.notcul)

        #QtCore.QObject.connect(self.button, QtCore.SIGNAL('clicked()'), self.hello)



    def add(self):
	read_uid = Read.run()
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(read_uid,))
	rows = cur.fetchall()
	conn.close()
	if not rows:
	    self.w = AddFrame.AddWindow(read_uid, self.csocket)
	    self.w.show()
	else:
	    print "이미등록된카드입니다."
	    return;
    def cul(self):
	read_uid = Read.run()
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(read_uid,))
	rows = cur.fetchall()
	conn.close()
	if not rows:
	    print "등록되지않은카드입니다."
	    return;
	else:
	    print rows[0][1]
	    self.csocket.send(("cul$"+str(rows[0][1])).encode())
	    #face_recog.run()

    def notcul(self):
	read_uid = Read.run()
	conn = sqlite3.connect("cul.db")
	cur = conn.cursor()
	cur.execute("select * from emp_list where uid = ?" ,(read_uid,))
	rows = cur.fetchall()
	conn.close()
	if not rows:
	    print "등록되지않은카드입니다."
	    return;
	else:
	    print rows[0][1]
	    self.csocket.send(("notcul$"+str(rows[0][1])).encode())
	    #face_recog.run()
    def create_Butt(self, msg,x,y,width,height,button3):
	button3 = QtGui.QPushButton(msg, self)
        button3.setGeometry(x, y, width, height)
        button3.clicked.connect(self.hello3)
	button3.setText("d")

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
