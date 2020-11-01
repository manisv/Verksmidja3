import time

import RPi.GPIO as GPIO  

from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'key'


ADAFRUIT_IO_USERNAME = 'username'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


led_pin = 6            

GPIO.setmode(GPIO.BCM)          
GPIO.setup(led_pin, GPIO.OUT)   

try: 
    digital = aio.feeds('digital')
except RequestError: 
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)



while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
        GPIO.output(led_pin,GPIO.HIGH)
    elif int(data.value) == 0:
        print('received <- OFF\n')
        GPIO.output(led_pin,GPIO.LOW)

    time.sleep(0.5)
