import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

TRIG = 23
ECHO = 24

print "hello"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

pwm=GPIO.PWM(22,100)
pwm.start(5)

angle1=10
duty1=float(angle1)/10+2.5

angle2=160
duty2=float(angle2)/10+2.5

ck=0
bk=0

while bk<=2:

  GPIO.output(TRIG,True)
  time.sleep(0.0001)
  GPIO.output(TRIG,False)
 
  print "start" 
 
  while ck<=2 :

     pwm.ChangeDutyCycle(duty1)
     time.sleep(2)
     pwm.ChangeDutyCycle(duty2)
     time.sleep(2)
  
     print "motor on"
     ck=ck+1

  GPIO.output(TRIG,True)
  time.sleep(0.0001)
  GPIO.output(TRIG,False)

  while GPIO.input(ECHO)==0:
       pulse_start = time.time()
  while GPIO.input(ECHO)==1:
       pulse_end = time.time() 

  print "sensor echo send"

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance,2)

  print "distance:" ,distance,"cm"

  bk=bk+1

time.sleep(1)

   

print(distance)
x = (distance)
y = str(x)
fb = open('/home/pi/test.txt','a+')
fb.write(y)
fb.write('\n')
fb.close() 

GPIO.cleanup()

