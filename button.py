import time

import RPi.GPIO as GPIO

from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'key'


ADAFRUIT_IO_USERNAME = 'username'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


try: 
    digital = aio.feeds('digital')
except RequestError: 
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_current = GPIO.input(12)


while True:
    button_state = GPIO.input(12)
    if button_state == 0:
        button_current = 1
    elif button_state == 1:
        button_current = 0

    print('Button -> ', button_current)
    aio.send(digital.key, button_current)


    time.sleep(1)
