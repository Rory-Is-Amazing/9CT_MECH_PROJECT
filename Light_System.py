from machine import Pin
import time

ledr = Pin(12, Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)
ledy = Pin(13, Pin.OUT)
ledg = Pin(14, Pin.OUT)
ledb = Pin(15, Pin.OUT)
while True:  # Loop forever
    ledr.value(1)  # Turn the LED ON
    ledy.value(1)
    ledg.value(1)
    ledb.value(1)
    time.sleep(2) # Go to sleep for 2 seconds
        
    ledr.value(0)  # Turn the LED OFF
    ledy.value(0)
    ledg.value(0)
    ledb.value(0)
    time.sleep(2) # Go to sleep for 2 seconds
