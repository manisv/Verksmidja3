import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM1",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):
  GPIO.output(pin,GPIO.HIGH)  
  time.sleep(1)  
  GPIO.output(pin,GPIO.LOW)  
  time.sleep(1)
  return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:

  read_ser=ser.readline()
  msg = read_ser.decode('utf-8') # To convert byte strings to Unicode, líka hægt að nota bytes.decode(read_ser)
  print(msg) 
  if(msg.strip()=="Hello From Arduino!"):
      blink(11)