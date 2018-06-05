import socket

#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#
import sys
import RPi.GPIO as GPIO
import MFRC522
import signal
import time
continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

#socket--------------------------------------------------------------------------------------------------------------------
def sendMsg(uid,date):
	ip = '192.168.0.8' 
    	port = 8888
    	addr = (ip,port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect(addr)
                uidDate = uid + ';' + date
		sock.send('add$3393'.encode())
                print('msg to server :' +  uidDate)
		msg = sock.recv(1024)
		print('msg from server: '  + msg.decode())
	except  Exception as e:
		print('error addr %s:%s'%addr)
		sys.exit()
	finally:
		sock.close()
#socket--------------------------------------------------------------------------------------------------------------------

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome messageprint ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")

#client run and RFID run--------------------------------------------------------------------------------------------------
def run():
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK: 
                date = time.ctime() #now datetime
                print ("Card detected")
                # Print UID
                print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
                AttachUid=  str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
                print("SUM_UID : " + AttachUid)

                sendMsg(AttachUid,date)

        time.sleep(2)

if __name__ == '__main__':
  run()
#client run and RFID run--------------------------------------------------------------------------------------------------
