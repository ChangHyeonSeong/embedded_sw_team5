import train
import sqlite3
from PySide import QtCore, QtGui
class AddWindow(QtGui.QWidget):
    def __init__(self, uid, csocket):
	self.sock = csocket
        QtGui.QWidget.__init__(self)
	self.read_uid = uid
        self.setWindowTitle("Click Window")
        self.setGeometry(300, 200, 300, 200)
	self.label_empid = QtGui.QLabel("input empid",self)
        self.label_empid.setGeometry(10,10,100,20)
	self.edit_empid = QtGui.QLineEdit(self)
	self.edit_empid.setGeometry(10,40,100,20)

        self.btn1 = QtGui.QPushButton('1', self)
        self.btn1.setGeometry(150, 10, 40, 40)
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2 = QtGui.QPushButton('2', self)
        self.btn2.setGeometry(190,10, 40, 40)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3 = QtGui.QPushButton('3', self)
        self.btn3.setGeometry(230, 10, 40, 40)
        self.btn3.clicked.connect(self.btn3Click)

        self.btn4 = QtGui.QPushButton('4', self)
        self.btn4.setGeometry(150, 50, 40, 40)
        self.btn4.clicked.connect(self.btn4Click)
        self.btn5 = QtGui.QPushButton('5', self)
        self.btn5.setGeometry(190, 50, 40, 40)
        self.btn5.clicked.connect(self.btn5Click)
        self.btn6 = QtGui.QPushButton('6', self)
        self.btn6.setGeometry(230, 50, 40, 40)
        self.btn6.clicked.connect(self.btn6Click)

        self.btn7 = QtGui.QPushButton('7', self)
        self.btn7.setGeometry(150, 90, 40, 40)
        self.btn7.clicked.connect(self.btn7Click)
        self.btn8 = QtGui.QPushButton('8', self)
        self.btn8.setGeometry(190, 90, 40, 40)
        self.btn8.clicked.connect(self.btn8Click)
        self.btn9 = QtGui.QPushButton('9', self)
        self.btn9.setGeometry(230, 90, 40, 40)
        self.btn9.clicked.connect(self.btn9Click)

        self.btn0 = QtGui.QPushButton('0', self)
        self.btn0.setGeometry(150, 130, 40, 40)
        self.btn0.clicked.connect(self.btn0Click)
        self.btnOk = QtGui.QPushButton('ok', self)
        self.btnOk.setGeometry(190, 130, 80, 40)
	self.btnOk.clicked.connect(self.btnOkClick)

    def btn0Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn0.text())
    def btn1Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn1.text())
    def btn2Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn2.text())
    def btn3Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn3.text())
    def btn4Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn4.text())
    def btn5Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn5.text())
    def btn6Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn6.text())
    def btn7Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn7.text())
    def btn8Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn8.text())
    def btn9Click(self):
	print self.edit_empid.text()
        self.edit_empid.setText(self.edit_empid.text()+self.btn9.text())
    def btnOkClick(self):
	empid = self.edit_empid.text()
	self.sock.send("Add$"+empid.encode())
	msg = self.sock.recv(1024)
	if msg == "AddOK":
		if train.run(empid):
			conn = sqlite3.connect("cul.db")
			cur = conn.cursor()
			cur.execute("INSERT INTO emp_list VALUES(?,?)" ,(self.read_uid,empid))
			conn.commit()
			conn.close()
			self.close()
		else:
			print"xxx"
	else :
		print "emp_id x"
