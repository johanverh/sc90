import RPi.GPIO as GPIO
import time

control = [2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,]

servo = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

p=GPIO.PWM(servo,50)# 50hz frequency

p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


try:
    while True:
        for x in range(20):
            p.ChangeDutyCycle(control[x])
            time.sleep(0.03)
            print (x)
             
        time.sleep(5)
           
        for x in range(16,0,-1):
            p.ChangeDutyCycle(control[x])
            time.sleep(0.03)
            print (x)
             
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()