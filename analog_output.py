import RPi.GPIO as GPIO     
from time import sleep  
from Adafruit_IO import Client, Feed, RequestError

led_pin = 21            

GPIO.setmode(GPIO.BCM)          
GPIO.setup(led_pin, GPIO.OUT)   
GPIO.setwarnings(False)

pwm = GPIO.PWM(led_pin, 100)    
pwm.start(0)                    
pwm.ChangeFrequency(60)
prev_read = 0

ADAFRUIT_IO_KEY = 'key'
 

ADAFRUIT_IO_USERNAME = 'username'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
 
try:
    analog = aio.feeds('analog')
except RequestError:
    feed = Feed(name='analog')
    analog = aio.create_feed(feed)

def map_range(x, in_min, in_max, out_min, out_max):
    """re-maps a number from one range to another."""
    mapped = (x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)
            
while True:
    analog_read = aio.receive(analog.key)
    if analog_read.value != prev_read:
        print('received <- ', analog_read.value)
        analog_value = map_range(int(analog_read.value), 0, 1024, 0, 100)
        pwm.ChangeDutyCycle(int(analog_value))
    prev_read = analog_read.value

    sleep(0.5)


pwm.stop()
GPIO.cleanup()