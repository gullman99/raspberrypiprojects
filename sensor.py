import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

for i in range(1000):
    if GPIO.input(4)==True:
        print 'intruder alert!'
    else:
        print 'no worries'
    time.sleep(1)


        
    

