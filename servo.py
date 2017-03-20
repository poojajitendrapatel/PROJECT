import RPi.GPIO as GPIO 
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)


pwm=GPIO.PWM(22,100)
pwm.start(5)

angle1=10
duty1=float(angle1)/10+2.5

angle2=160
duty2=float(angle2)/10+2.5

ck=0
while ck<=10:
     pwm.ChangeDutyCycle(duty1)
     time.sleep(2)
     pwm.ChangeDutyCycle(duty2)
     time.sleep(2)
     ck=ck+1
time.sleep(1)
GPIO.cleanup()
