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
pwm.start(left)
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
    

def servoPosition(angle):
    dc = left + (angle * one_degree)
    print ("Angle %d DutyCycle %f" %(angle, dc))
    pwm.ChangeDutyCycle(dc)
    






try:
    while True:
        angle = 0
        while (angle <= 180):
            setAngle(angle, 0.05)
            angle += 5
        
        while (angle >= 0):
            setAngle(angle, 0.07)
            angle -= 5
    
        setAngle(0,1)
        setAngle(90,1)
        setAngle(180,1)
        setAngle(150,1)
        setAngle(120,1)
        setAngle(90,1)
        setAngle(30,1)
        setAngle(60,1)
        setAngle(0,1)
        
        setAngle(45,1.5)
        setAngle(90,1.5)
        setAngle(135,1.5)
        setAngle(180,1.5)
        setAngle(0,2)
    
    
    
    
    #servoPosition(180,1)
    #sleep(5)
    
    #servoPosition(30)
    #sleep(5)
    
    #servoPosition(150)
    #sleep(5)
    
    #servoPosition(60)
    #sleep(5)
    
    #servoPosition(120)
    #sleep(5)
    
    #servoPosition(90)
    #sleep(5)
        
    #servoPosition(0)
    #sleep(1)


    #pwm.stop
    #GPIO.cleanup()
    
except KeyboardInterrupt:
    # Stop PWM op GPIO
    pwm.stop
    # GPIO netjes afsluiten
    GPIO.cleanup()
