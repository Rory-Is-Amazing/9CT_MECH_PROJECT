import machine
import time
from machine import Pin

speaker = machine.PWM(machine.Pin(6))

ts = 0

ledr = Pin(12, Pin.OUT)
ledy = Pin(13, Pin.OUT)
ledg = Pin(14, Pin.OUT)
ledb = Pin(15, Pin.OUT)

ts1 = Pin(16, Pin.IN, Pin.PULL_DOWN)

sensor1 = 0
sensor2 = 1
sensor3 = 1
def main():
    while True:
        sensor1 = 1
        sensor2 = 1
        sensor3 = 1
        
        ts = (sensor1 + sensor2 + sensor3)
        
        ledr.value(0)
        ledy.value(0)
        ledg.value(0)
        ledb.value(0)
        if ts == 0:
            red()
        elif ts == 1:
            yellow()
        elif ts == 2:
            green()
        elif ts == 3:
            blue()
        else:
            print("Error.")
            break

def play_tone(frequency, duration):
    if frequency == 0:
        speaker.duty_u16(0) # Turn off buzzer
    else:
        speaker.freq(frequency) 
        speaker.duty_u16(32768) # Set buzzer volume to 50%
        
    time.sleep(duration)
    speaker.duty_u16(0) # Turn off buzzer

def red():
    print()
    time.sleep(0.25)
    ledr.value(1)
    play_tone(1000,0.25)
    time.sleep(0.25)
def yellow():
    print('yellow')
    time.sleep(0.125)
    ledy.value(1)
    play_tone(1000,0.125)
    time.sleep(0.125)
def green():
    print('green')
    time.sleep(0.0625)
    ledg.value(1)
    play_tone(1000,0.0625)
    time.sleep(0.0625)
def blue():
    print('blue')
    time.sleep(0.03125)
    ledb.value(1)
    play_tone(1000,0.03125)
    time.sleep(0.03125)
'''
while True:
    time.sleep(0.5)
    play_tone(3000,0.5)
'''


if __name__ == "__main__":
    main()

speaker.deinit()
