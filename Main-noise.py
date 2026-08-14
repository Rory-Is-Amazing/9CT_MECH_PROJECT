import machine
import time
from machine import Pin

ledr = Pin(12, Pin.OUT)
ledy = Pin(13, Pin.OUT)
ledg = Pin(14, Pin.OUT)
ledb = Pin(15, Pin.OUT)

ts1 = Pin(17, Pin.IN, Pin.PULL_DOWN)
ts2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(20, Pin.IN, Pin.PULL_DOWN)

sw = Pin(27, Pin.IN, Pin.PULL_UP)

def main():
    while True:
        if sw.value() == 0:
            ts = ts1.value() + ts2.value() + ts3.value()

            ledr.value(0)
            ledy.value(0)
            ledg.value(0)
            ledb.value(0)

            if ts == 0:
                ledr.value(1)
                time.sleep(0.25)

            elif ts == 1:
                ledy.value(1)
                time.sleep(0.125)

            elif ts == 2:
                ledg.value(1)
                time.sleep(0.0625)

            elif ts == 3:
                ledb.value(1)
                time.sleep(0.03125)
            else:
                print("Error: Invalid tilt sensor value")
        elif sw.value() == 1:
            ledr.value(0)
            ledy.value(0)
            ledg.value(0)
            ledb.value(0)
        else:
            print("Error: Invalid switch value")

if __name__ == "__main__":
    main()

