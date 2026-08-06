import machine
import time
from machine import Pin

speaker = machine.PWM(machine.Pin(6))

ts = 0

ledr = Pin(12, Pin.OUT)
ledy = Pin(13, Pin.OUT)
ledg = Pin(14, Pin.OUT)
ledb = Pin(15, Pin.OUT)

sensor1 = 0
sensor2 = 1
sensor3 = 1
def main():
    while True:
        #Sens
        sensor1 = 1
        sensor2 = 17
        sensor3 = 0
        
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
    ledr.value(1)
    time.sleep(2)
def yellow():
    print('yellow')
    ledy.value(1)
    time.sleep(2)
def green():
    print('green')
    ledg.value(1)
    time.sleep(2)
def blue():
    print('blue')
    ledb.value(1)
    time.sleep(2)
'''
while True:
    time.sleep(0.5)
    play_tone(3000,0.5)
'''


if __name__ == "__main__":
    main()

speaker.deinit()