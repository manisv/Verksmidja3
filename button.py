"""
'digital_in.py'
==================================
Example of sending button values
to an Adafruit IO feed.

Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time

import RPi.GPIO as GPIO

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_tXUs36pUccPEqWQ4RVQRsu6GDqXp'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'manisv'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def button_callback(channel):
    print("Button was pushed!")

try: # if we have a 'digital' feed
    digital = aio.feeds('digital')
except RequestError: # create a digital feed
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)

# button set up
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
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

    # avoid timeout from adafruit io
    time.sleep(1)