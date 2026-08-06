import machine
import time

speaker = machine.PWM(machine.Pin(6)) # Set up the PWM pin (GP15)

def main():
    

def play_tone(frequency, duration):
    if frequency == 0:
        speaker.duty_u16(0) # Turn off buzzer
    else:
        speaker.freq(frequency) 
        speaker.duty_u16(32768) # Set buzzer volume to 50%
        
    time.sleep(duration)
    speaker.duty_u16(0) # Turn off buzzer

while True:
    time.sleep(0.5)
    play_tone(3000,0.5)
# G5

# Always deinitialize PWM when done
speaker.deinit()

if __name__ == "__main__":
    main()

