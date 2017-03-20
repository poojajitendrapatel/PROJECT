import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG=23
ECHO=24

print "distance calculation"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
  GPIO.output(TRIG,True)
  time.sleep(0.0001)
  GPIO.output(TRIG,False)
  print "start"
   

  while GPIO.input(ECHO)==0:
       pulse_start = time.time()

  while GPIO.input(ECHO)==1:
       pulse_end = time.time()
    
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance,2)
    
  print "distance:" ,distance,"cm"
   
  time.sleep(1)
 
 
  print(distance)
  x = (distance)
  y = str(x)
  fb = open('/home/pi/test.txt','a+')
  fb.write(y)
  fb.write('\t')
  fb.close()

GPIO.cleanup()
