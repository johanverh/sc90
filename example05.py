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
pwm=GPIO.PWM(servo,50)

left = 2.2
right = 11.9
# Start PWM op de GPIO pin met duty-cycle van 6%
pwm.start(4.25)
sleep(2)
one_degree = 0.048889

def setAngle(angle, wait):
    dutyCycle = (angle / 18) + 2.2
    dutyCycle = (angle * 0.05) + 2
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(dutyCycle)
    print ("Angle %d DutyCycle %f" %(angle, dutyCycle))
    sleep(wait)
    GPIO.output(servo, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        angle = 45
        while (angle <= 120):
            setAngle(angle, 0.09)
            angle += 15
        
        while (angle >= 45):
            setAngle(angle, 0.09)
            angle -= 15
    

    #pwm.stop
    #GPIO.cleanup()
    
except KeyboardInterrupt:
    # Stop PWM op GPIO
    pwm.stop
    # GPIO netjes afsluiten
    GPIO.cleanup()

