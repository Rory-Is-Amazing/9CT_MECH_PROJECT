import machine
import time
from machine import Pin

ts1 = Pin(16, Pin.IN, Pin.PULL_DOWN)
ts2 = Pin(17, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(18, Pin.IN, Pin.PULL_DOWN)

while True:
        if ts1.value() == 0:
            print("It works1")
            time.sleep(1)
        if ts2.value() == 0:
            print("It works2")
            time.sleep(1)
        if ts3.value() == 0:
            print("It works3")
            time.sleep(1)