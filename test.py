import machine
import time
from machine import Pin

ts1 = Pin(17, Pin.IN, Pin.PULL_DOWN)
ts2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
while True:
    print(ts1.value(), " ", ts2.value(), " ", ts3.value(), " ", )
    time.sleep(1)