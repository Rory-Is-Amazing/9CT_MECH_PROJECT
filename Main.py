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

ledr.value(0)
ledy.value(0)
ledg.value(0)
ledb.value(0)

def play_tone(freq, dur):
    if freq == 0:
        speaker.duty_u16(0)
    else:
        speaker.freq(freq)
        speaker.duty_u16(32768)
    time.sleep(dur)
    speaker.duty_u16(0)
def main():
    while True:
            ts = ts1.value() + ts2.value() + ts3.value()

            ledr.value(0)
            ledy.value(0)
            ledg.value(0)
            ledb.value(0)

            if ts == 0:
                ledr.value(1)
                play_tone(1000, 0.25)
                time.sleep(0.25)

            elif ts == 1:
                ledy.value(1)
                play_tone(1000, 0.125)
                time.sleep(0.125)

            elif ts == 2:
                ledg.value(1)
                play_tone(1000, 0.0625)
                time.sleep(0.0625)

            elif ts == 3:
                ledb.value(1)
                play_tone(1000, 0.03125)
                time.sleep(0.03125)
            else:
                print("Error: Invalid tilt sensor value")


if __name__ == "__main__":
    main()

speaker.deinit()