#!/bin/python

# importeer de GPIO bibliotheek
import RPi.GPIO as GPIO
# importeer de time bibliotheek voor tijdfuncties
from time import sleep

# Zet de pinmmode op Broadcom BCM
GPIO.setmode(GPIO.BCM)
# Zet waarschuwingen uit
GPIO.setwarnings(False)

# GPIO voor servo
servo = 5
# Zet GPIO pin als uitgang
GPIO.setup(servo,GPIO.OUT)
# Configureer de pin voor PWM met een frequentie van 50 hz
p=GPIO.PWM(servo,50)

# Start PWM op de GPIO pin met duty-cycle van 6%
p.start(6)
sleep(4)
p.ChangeDutyCycle(2)
sleep(4)
p.ChangeDutyCycle(6)
sleep(4)
p.ChangeDutyCycle(11)
sleep(4)

# Stop PWM op GPIO
p.stop
# GPIO netjes afsluiten
GPIO.cleanup()