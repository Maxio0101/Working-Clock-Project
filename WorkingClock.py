#!/usr/bin/env python
# -*- coding: utf8 -*-
# Working Hourse Record:Read RFID Tag, and Record StaffID, Day, start time, end time and duration hours
#                        into database
# When one card is detected, white LED is flash.
# If the card is authenticated, you will hear "Bi~".
#

import time
import RPi.GPIO as GPIO
import MFRC522
import signal
import serial
from datetime import date, datetime
from TimeRecord import TimeRecord
import os


GPIO.setmode(GPIO.BOARD)

#pin setting
Bezzer = 7   
LED1 = 11
counter = 0

#output pin setting
GPIO.setup(Bezzer, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)


continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def close_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, close App.")
    continue_reading = False
    GPIO.cleanup()
    
def log_write(StaffID, today, currentTime):
    '''
    Recod time stamp in Raspberry pi 
    '''
    try:
        with open("../MFRC522-python/WTStampLogger.txt", "a") as temp:
            temp.write(str(StaffID)+"@"+str(time.time())+"@"+today+"@"+str(now)+'\n')
    except IOError as err:
        print(err)
    finally:
        temp.close()


                    



# Hook the SIGINT
signal.signal(signal.SIGINT, close_read)

# Create an object of the class MFRC522
CardReader = MFRC522.MFRC522()
BLOCK_ADDRS = [8, 9, 10]

# Welcome message
print ("Welcome to the working clock!")
print ("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = CardReader.MFRC522_Request(CardReader.PICC_REQIDL)

    # If a card is found
    if status == CardReader.MI_OK:
        #print ("Card detected")
        
        GPIO.output(LED1,GPIO.High) #LED on
    
    # Get the UID of the card
        (status,uid) = CardReader.MFRC522_Anticoll()
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        # Select the scanned tag
        CardReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = CardReader.MFRC522_Auth(CardReader.PICC_AUTHENT1A, 8, key, uid)
        block = CardReader.MFRC522_Read(8) 
        
        # Get staff ID
        StaffID = ''.join(chr(block[i]) for i in range(0,7))
        
        if StaffID[0:5] == "SSD00": # Authenticate check
            #print ("StaffID"+str(StaffID))
            #Get Day
            today = date.today().strftime("%Y-%m-%d")
            #Get current ime
            now = datetime.now()
            currentTime = now.strftime("%H:%M:%S.%f")
            
            log_write(StaffID, today, currentTime)
            
            #Record Time into DB
            #Check if have start time
            startTime_tuple = TimeRecord().get_startTime(staffID, today)
            
            if startTime_tuple is None:
                TimeRecord().add_startTime(staffID, today, currentTime)
            else:
                TimeRecord().calculate_duration(startTime_tuple, now)

            TimeRecord().close_db()
                
                    
            GPIO.output(Bezzer,GPIO.HIGH) 
            time.sleep(0.2)
            
            CardReader.MFRC522_StopCrypto1()
            GPIO.output(Bezzer,GPIO.LOW)
            
            
            GPIO.output(LED1,GPIO.LOW) #LED off
            time.sleep(0.5)
            #print (text[1])
        else:
            print ("Authentication error")
            GPIO.output(LED1,GPIO.HIGH) #LED on
            time.sleep(0.5)
            GPIO.output(LED1,GPIO.LOW) #LED off

   