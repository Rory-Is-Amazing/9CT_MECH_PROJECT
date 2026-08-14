from machine import Pin
from time import sleep

# Initialize the tilt switch pin with an internal pull-up resistor
tilt = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    # Read the tilt value and mirror it to the LED
    led.value(tilt.value())
    sleep(1)
    if tilt.value() == 1:
        print("1")
    else:
        print("2")
