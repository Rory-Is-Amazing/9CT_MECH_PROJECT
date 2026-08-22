#Sets up Libarries
import machine
import time
from machine import Pin

buzzer = machine.PWM(machine.Pin(6)) #Set up the buzzer
#                  ^ Sets up as PWM, to allow for frquency change

ledr = Pin(12, Pin.OUT) #Red LED Set up as a output
ledy = Pin(13, Pin.OUT) #Yellow
ledg = Pin(14, Pin.OUT) #Green
ledb = Pin(15, Pin.OUT) #Blue

ts1 = Pin(17, Pin.IN, Pin.PULL_DOWN) #Set up the tilt sensors as inputs
ts2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(20, Pin.IN, Pin.PULL_DOWN)

ledr.value(0) #Set all the LEDs to OFF
ledy.value(0)
ledg.value(0)
ledb.value(0)

'''
The purpose of the play_tone() function is to make the buzzer produce a sound
at the chosen frequency and amount of time declared elsewhere then turn it off.
'''
def play_tone(frequency, length):
    if frequency == 0: #If the frequency is set to 0, then the buzzer will not make a sound
        buzzer.duty_u16(0) # Setting duty to 0 turns the buzzer OFF
    else: #otherwise:
        buzzer.freq(frequency) #Set the buzzer to the frequency passed in by external code
        buzzer.duty_u16(32768) #50% volume
    time.sleep(length) #puase for time passed in by external code
    buzzer.duty_u16(0) # Setting duty to zero turns the buzzer OFF
    
def main():
    while True:
        ts = 0
        
        ledr.value(0) #Set all the LEDs to OFF
        ledy.value(0)
        ledg.value(0)
        ledb.value(0)
        '''
        Combines tilt switch values, into their specific ranges,
        to allow for the correct LED to light up and that the 
        buzzer and LED beep to the correct frequency.
        '''
        ts = ts1.value() + ts2.value() + ts3.value() #All 3 tilt switchs are added together to create an angle range (value of 0-3).

        #That vangle range then determines which colour of LED is outputed and the frequency of the buzzer and LED beeping/flashing
        if ts == 0:
            red() #far away from flat range
        elif ts == 1:
            yellow()#further away from flat range
        elif ts == 2:
            green() # closer to flat range
        elif ts == 3:
            blue() # close to or flat range
        else:
            print("Error: Invalid tilt sensor value")
'''
These functions are reperesenative of each angle range, Red - A, Yellow - B, Green - C, Blue - D.
'''
def red(): #Slowest Beeping, indicating the device is further away from flat
    ledr.value(1)
    play_tone(3000, 0.25) #Here the frequency and duration of beep is set, before being reset and turned off in the play_tone() function
    time.sleep(0.25)
    ledr.value(0)

def yellow(): # Medium Beeping, indicating the device is further away from flat
    ledy.value(1)
    play_tone(3000, 0.125)
    time.sleep(0.125)
    ledy.value(0)

def green(): # Faster Beeping, indicating the device is closer to flat
    ledg.value(1)
    play_tone(3000, 0.0625)
    time.sleep(0.0625)
    ledg.value(0)   

def blue(): # Fastest Beeping, indicating the device is close to or flat
    ledb.value(1)
    play_tone(3000, 0.03125)
    time.sleep(0.03125)
    ledb.value(0)
    
if __name__ == "__main__": #controls when the program starts so it only runs when this file is the one being run
    main()

speaker.deinit() #prevents the speaker from contuily buzzing
