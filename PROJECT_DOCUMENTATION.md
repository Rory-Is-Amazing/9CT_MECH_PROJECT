# Requirements Outline
### The Need 
Precision is a foundational aspect across industries such as construction, production, engineering, surveying, and techical trades. In these enviroments/work paces even deviations of a few degrees can compromise work flow in ways such as construction integraty, allighnment, safety, or downstream practcies. A misalignement of even 5° can:
- Cause structural components to sit incorrectly
- Lead to cumulative measurement errors
- Reduce the integrity of joints or welds
- Create unsafe load distributions
- Compromise the accuracy of machinery setups

Traditional levels rely on bubbles/secondary liquid suspended in amain liquid, leading to 3 main limitations:
- Low resoloution (the bubble only provides approixamet orientation) 
- No auditory feedback (users must maintain visual monotoring)
- Poor usability in low‑light or obstructed environments

In modern industry, the need for high precision orientation tools has increased significantly, giving birth to the digital level (a similar product to my proposed soloution). These industries all rely on tools which are able to provide:

- Higher resolution feedback (more than a liquid bubble can provide)
- Responsiveness (capable of detecting small angular changes)
- Multiple outputs (visual and auditory, for use in noisy or low‑visibility conditions, and to provide use ease)
- Hands‑free interpretability (allows workers to maintain focus on tasks)
- Fast sampling and real‑time correction (accuaracy)
- Repeatability (consistent readings across different environments)

### Proposed Soloution
I will design an eletronic level, which through use of a Raspberry Pi Pico Microcontroller, to process inputs from 3 differently orientated tilt switchs to accurately determine the orientation of the devise accurately. Then 4 LEDs (Red, Yellow, Green and Blue) as well as a buzzer will provide visual and auditory feedback to the orientation, witht the closer to flat, the faster the buzzer and LED beeps, as well as which LED beeping providing further feedback to the accuracy of orientation.

0-5° (Flat) - Buzzer and Blue LED beeping/flashing fastest
5-10° (Close to Fflat) - Buzzer and Green LED beeping/flashing faster
10-20° (Further from flat) - Buzzer and Yellow LED beeping/flashing slower
20+° (Far from flat) - Buzzer and Red LED beeping/flashing slowest

### Key Actions
#### Action 1 - Tilt switchs

3 tilt switches acts as binary sensors, acting as on/off switches depending on the orientation. By using three switches they are able to measure four specific angel ranges. Then communicating their status to the microcontoler, to than be combined for output. The sampling interval is as low as every 0.5 seconds while its orientation is far from flat, too as fast as a 0.0625 second sampling interval while it is closer to flat.

#### Action 2 - LEDs (Red, Yellow, Green, and Blue)
LEDs light up depending on angle range provided by tilt switches:

If between 0-5° (Angle Range D), Blue LED beeps every 0.0625 seconds.

If between 5-10° (Angle Range C), Green LED beeps every 0.125 seconds.

if between 10-20° (Angle Range B), Yellow LED beeps every 0.25 seconds.

If above 20° (Angle Range A), Red LED beeps every 0.5 seconds.

#### Action 3 - Buzzer
Simlilarily to LEDs, buzzer beeps depending on angle range provided by tilt switches, staying in time with LEDs:

If between 0-5° (D), Buzzer beeps every 0.0625 seconds.

If between 5-10° (C), Buzzer beeps every 0.125 seconds.

if between 10-20°(B), Buzzer beeps every 0.25 seconds.

If above 20° (A), Buzzer beeps every 0.5 seconds.


### Functional Requirments
### Tilt Switchs Input Functional Requirments:
- The system will be required to read on/off state of all 3 tilt switches at a sampling interval of as low as 0.0625 seconds, up to 0.5 seconds
- The system will be required to determine which of one of 4 angle ranges (A, B, C or D) by combining on/off states of the 3 tilt switches
- The system will be required to store the detected angle range (A, B, C or D) for use by the LEDs and Buzzer subroutine
#### LED Output Functional Requirments
- The system will be required to turn on one of the 4 LEDs (red, yellow, green, and blue) based on the detected angle range. Blue for 0–5° (D), Green for 5–10° (C), Yellow for 10–20° (B), and Red for above 20° (A).
- The system will be required to flash the active LED (red, yellow, green, or blue) at the assoociated interval for the detected range : 0.0625 seconds (D), 0.125 seconds (C), 0.25 seconds (B), or 0.5 seconds (A).
- The system will be required to flash the LED (red, yellow, green, or blue) synchronised with the buzzer timing for the same angle range.
#### Buzzer Output Functional Requirments
- The system will be required to create a beep whenever an angle range (A, B, C or D) is detected
- The system will be required to beep at the the assoociated interval for the detected range: 0.0625 seconds (D), 0.125 seconds (C), 0.25 seconds (B), or 0.5 seconds (A).
- The system will be required to flash the buzzer synchronised with the LED timing for the same angle range.
### Test Case
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| >20° angle of system tilt sensor reading (Angle Range A) | 0/3 Tilt Switches On | System reads tilt switch states, identifying the ON/OFF patern to associated angle range (>20°) |
| 10-20° angle of system tilt sensor reading (Angle Range B) | 1/3 Tilt Switches On | System reads tilt switch states, identifying the ON/OFF patern to associated angle range (10-20°) |
| 5-10° angle of system tilt sensor reading (Angle Range C) | 2/3 Tilt Switches On| System reads tilt switch states, identifying the ON/OFF patern to associated angle range (5-10°) |
| 0-5° angle of system tilt sensor reading (Angle Range D) | 3/3 Tilt Switches On | System reads tilt switch states, identifying the ON/OFF patern to associated angle range (0-5°) |
| LED Output for Placeholder Range A | System Receives Placeholder Value of range A ( 0/3 tilt switchs on) | System turns on Red LED and flashes LED every 0.5 |
| LED Output for Placeholder Range B | System Receives Placeholder Value of range B ( 1/3 tilt switchs on) | System turns on Yellow LED and flashes LED every 0.25 |
| LED Output for Placeholder Range C | System Receives Placeholder Value of range C ( 2/3 tilt switchs on) | System turns on Green LED and flashes LED every 0.125 |
| LED Output for Placeholder Range D | System Receives Placeholder Value of range D ( 3/3 tilt switchs on) | System turns on Blue LED and flashes LED every 0.0625 |
| Buzzer Output for Placeholder Range A | System Receives Placeholder Value of range of A ( 0/3 tilt switchs on) | System activates buzzer and beeps at a 0.5 second interval |
| Buzzer Output for Placeholder Range B | System Receives Placeholder Value of range of B ( 1/3 tilt switchs on) | System activates buzzer and beeps at a 0.25 second interval |
| Buzzer Output for Placeholder Range C | System Receives Placeholder Value ofrange of C ( 2/3 tilt switchs on) | System activates buzzer and beeps at a 0.125 second interval |
| Buzzer Output for Placeholder Range D | System Receives Placeholder Value of range D ( 3/3 tilt switchs on) | System activates buzzer and beeps at a 0.0625 second interval |
| LED and Buzzer Synchronised Output for Placeholder Range A | System Receives Placeholder Value of range A ( 3/3 tilt switchs on) | System activates buzzer and Red LED and beeps/flashes at a 0.5 second interval |
| LED and Buzzer Synchronised Output for Placeholder Range B | System Receives Placeholder Value of range B ( 3/3 tilt switchs on) | System activates buzzer and Yellow LED and beeps/flashes at a 0.25 second interval |
| LED and Buzzer Synchronised Output for Placeholder Range C | System Receives Placeholder Value of range C ( 3/3 tilt switchs on) | System activates buzzer and Green LED and beeps/flashes at a 0.125 second interval |
| LED and Buzzer Synchronised Output for Placeholder Range D | System Receives Placeholder Value of range D ( 3/3 tilt switchs on) | System activates buzzer and Blue LED and beeps/flashes at a 0.0625 second interval |
| Full System Combined Behaviour for >20° angle of system | 0/3 Tilt Switches On | System activates buzzer and Red LED and beeps/flashes at a 0.5 second interval |
| Full System Combined Behaviour for 10-20° angle of system | 1/3 Tilt Switches On | System activates buzzer and Yellow LED and beeps/flashes at a 0.25 second interval |
| Full System Combined Behaviour for 5-10° angle of system | 2/3 Tilt Switches On | System activates buzzer and Green LED and beeps/flashes at a 0.125 second interval |
| Full System Combined Behaviour for 0-5° angle of system | 3/3 Tilt Switches On | System activates buzzer and Blue LED and beeps/flashes at a 0.0625 second interval |
### Non-Functional Requirments
#### Efficiency:
- The system will run code that is written to minimise unnecessary processing, ensuring that tilt‑switch readings, LED control, and buzzer output are handled efficiently
- My system will be required to maintain stable connection with inputs, to keep up with speed of outputs and computation. 
- My system will be required to update outputs without causing noticeable/observable lag or missed cycles, over longer periods of operation.

#### Response Time:
- My system will be required to respond to changes in tilt switch states immediatly after receiving input, providing an output by updating the LEDs and buzzer.
- My system will take input from tilt switches at a sampling interval appropriate to the detected angle range (0.5, 0.25, 0.125, 0.0625)

#### Accuracy:
- The system will be required to correctly interpret the ON/OFF states of the 3 tilt switches, and calculate the correct angle range, being able to accuratly repeat this step many times a second, over an extended period of time.
- The system will produce LED and buzzer outputs that match the calculated angle range with no incorrect activation.
- The system will maintain synchronisation between LED flashes and buzzer beeps, accuratly over an extended period of time.
# Design
### Flow Charts: 
#### Main Function, 4 Output Functions
![Main Function, 4 Output Functions](Main-Function,-and-4-Output-Functions.png)
#### Speaker Function
![Speaker Function](Speaker-Function.png)
### Pseudo Code:
#### Main Function, 4 Output Functions, Speaker Function
```
BEGIN play_tone(frequency, length)

    IF frequency == 0 THEN
        SET speaker duty to 0
    ELSE
        SET speaker frequency to frequency
        SET speaker duty to 50%
    END IF
    WAIT for length seconds
    SET speaker duty to 0

END play_tone(frequency, length)

BEGIN
    WHILE true
        READ switchs_on
        If switchs_on == 0 THEN
            red()
        ELSE IF switchs_on == 1 THEN
            yellow()
        ELSE IF switchs_on == 2 THEN
            green()
        ELSE IF switchs_on == 3 THEN
            blue()
        ELSE
            DISPLAY "Error."
        ENDIF
    ENDWHILE

BEGIN red()
    OUTPUT red_led.value(1)
    OUTPUT speaker.on(freq.fastest)
END red()

BEGIN yellow()
    OUTPUT yellow_led.value(1)
    OUTPUT speaker.on(freq.faster)
END yellow()

BEGIN green()
    OUTPUT green_led.value(1)
    OUTPUT speaker.on(freq.slower)
END green()

BEGIN blue()
    OUTPUT blue_led.value(1)
    OUTPUT speaker.on(freq.slowest)
END blue()
```

# Development and Integration
### First Prototype
```
import machine
import time
from machine import Pin

speaker = machine.PWM(machine.Pin(6))

ledr = Pin(12, Pin.OUT) # Red LED setup
ledy = Pin(13, Pin.OUT) # Yellow
ledg = Pin(14, Pin.OUT) # Green
ledb = Pin(15, Pin.OUT) # Blue

def main():
    while True:

        sensor1 = 0 #Placeholder values for coming tilt switches
        sensor2 = 0
        sensor3 = 0
        
        ts = (sensor1 + sensor2 + sensor3)

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
'''
These functions are reperesenative of each angle range, Red - A, Yellow - B, Green - C, Blue - D.
def red():
    print('red')
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

if __name__ == "__main__":
    main()
```
My original prototype code turned out similar to my final product, as my design phase really helped me in creating an effective peice of code, that almost worked perfectly with little change. The structure of my code turned out suprisingly simple and efficient for what it is to execute.
# Testing and Debugging
## Test Cases
### Test Case 1- LED Output
This Test Case is a combination of the Test Cases listed above in Requirments Outline including:
- LED Output for Placeholder Range A
- LED Output for Placeholder Range B
- LED Output for Placeholder Range C
- LED Output for Placeholder Range D
As they are all simliar test cases relating to the same code.

#### Plan Outline
Not much code adjustment and testing is required for this test case, as my first prototype almost acheived the requirments outline.
The following points are objectives that need to be adjusted in my prototype for my system to reach what is defined in my functional/non-functional requirments:
- Single LED activation (1 LED at a time)
- Creation and Correction of flash intervals
- Debug Visibility
#### Code Adjustment and Testing
In order for Single LED activation to be acheived I simply had to set the Value of the 4 LEDs to 0:
```   
ledr.value(0)
ledy.value(0)
ledg.value(0)
ledb.value(0)
```
I used this peice of code at the start of my Main, and inside my fain function while loop. This peice of code made it certian that only one light was on at a time.

This peice of code also aided in the meeting of the flashing requirment, where to adjust the flashing speed to match each angle range, I just kept halving the slowest beep leaving me with the red LED flashing at 0.5, the yellow at 0.25, green at 0.125 and blue at 0.0625. 
```
def red():
    print('red')
    ledr.value(1)
    time.sleep(0.5)
def yellow():
    print('yellow')
    ledy.value(1)
    time.sleep(0.25)
def green():
    print('green')
    ledg.value(0.125)
    time.sleep(2)
def blue():
    print('blue')
    ledb.value(1)
    time.sleep(0.0625)
```
Now depending on the placeholder input, a diffirentiatable flash speed would be ouputed by a single LED.

Finaly I removed the "print('colour')" peices of code which where there as a placeholder while the LED wiring wasn't set up.
```
def red():
    ledr.value(1)
    time.sleep(0.5)
def yellow():
    ledy.value(1)
    time.sleep(0.25)
def green():
    ledg.value(0.125)
    time.sleep(2)
def blue():
    ledb.value(1)
    time.sleep(0.0625)
```
#### Evaluation
This process included a few code adjustments that ran mostly smoothly, where I only had to test a few alternates before I met the LED test cases, and their functional and non-functional requirments. I effectively met both requirment sets, the LEDs operating like planned, flashing at the pace set earlier, and making sure only 1 of the 4 LEDs are on at a time. The entire process went particulary well with no hiccups within the coding aspect, I was challenged with wiring up 4 LEDs in such a small area using, resisitors and a wire each, meaning I had to get creative with my wiring. An area of my code that could be improved based on thes results, are once the buzzer is added to the system, and code implemented, making sure that the buzzer beeps at the same rate the LEDs flash, so changing the speed depending on the given angle range placeholder, and then tilt switch input.
### Test Case 2 - Buzzer Output (Function & Buzzer Operation)
#### Plan Outline
Not much code adjustment and testing is required for this test case, as my first prototype almost acheived the requirments outline.
The following points are objectives that need to be adjusted in my prototype for my system to reach what is defined in my functional/non-functional requirments:
- Buzzer Addition
- Buzzer Implemnation into LED output code
- Buzzer beeping Syncronisation with LED flashing 
#### Code Adjustment and Testing
Implimenting my buzzer into my code, was easy once wired up, simply putting in the playtone function I made for my prototype (The function makes the buzzer produce a sound at the chosen frequency and amount of time declared elsewhere then turn it off) just beside the LED on code.
```
def red():
    ledr.value(1)
    play_tone(3000, 1)
    time.sleep(0.5)
    ledr.value(0)

def yellow():
    ledy.value(1)
    play_tone(3000, 1)
    time.sleep(0.25)
    ledy.value(0)

def green():
    ledg.value(1)
    play_tone(3000, 1)
    time.sleep(0.125)
    ledg.value(0)   

def blue():
    ledb.value(1)
    play_tone(3000, 1)
    time.sleep(0.6125)
    ledb.value(0)
```
The Buzzer and LEDs beep/flashed together, but there is the timing issue with all the buzzers going off for 1 second.

I fixed the timing issue, by dividing the original duration the LED was on over both the LEDs duration and Buzzers duration, so the LED is on for twice the length the Buzzer beeps for, that duration being the original LED length:
```
def red():
    ledr.value(1)
    play_tone(1000, 0.25)
    time.sleep(0.25)
    ledr.value(0)

def yellow():
    ledy.value(1)
    play_tone(1000, 0.125)
    time.sleep(0.125)
    ledy.value(0)

def green():
    ledg.value(1)
    play_tone(1000, 0.0625)
    time.sleep(0.0625)
    ledg.value(0)   

def blue():
    ledb.value(1)
    play_tone(1000, 1)
    time.sleep(0.03125)
    ledb.value(0)
```
A small bug I experienced with the speaker (and LED but I couldnt find a soloution as easy, and it is less annoying) is that it would stay on after the system was turned off, and after some reasearch, I found `speaker.deinit()` which turns off the speaker as it is disconnected.
#### Evaluation
This process went similar to that of the LED, as once I set up the Buzzer I mainly just built onto the LEDs code. I effectively met both requirment sets, the Buzzer operated like planned, beeping at the pace set earlier, and making sure to stay in time with 1 of the 4 LEDs. The entire process went particulary well with no hiccups, apart from the bug solved with `speaker.deinit()`. An area of my code that could be improved is implementing a nicer buzzer sound/speed for the final buzzer.
### Test Case 3 - Tilt Switches
This Test Case is a combination of the Test Cases listed above in Requirments Outline including:
- Full System Combined Behaviour for +20° angle of system
- Full System Combined Behaviour for 10-20° angle of system 
- Full System Combined Behaviour for 5-10° angle of system
- Full System Combined Behaviour for 0-5° angle of system
As they are all simliar test cases relating to the same code.
#### Plan Outline
The following points are objectives that need to be adjusted in my prototype for my system to reach what is defined in my functional/non-functional requirments:
- Wire up Tilt Switchs to Bread Board
- Select Tilt Switch Orientations for Physical Level
- Set Up Tilt Switch code
- Test for Working Tilt Switch Input
#### Code Adjustment and Testing
Set up Tilt Switchs spread 1 pin space away from one another for ease to check if the sensors will work, code and pin set up:
```
ts1 = Pin(16, Pin.IN, Pin.PULL_DOWN)
ts2 = Pin(17, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(18, Pin.IN, Pin.PULL_DOWN)
```
I started testing the Tilt Switches in a seperate placeholder file using this code:
```
while True:
    print(ts1.value(), " ", ts2.value(), " ", ts3.value(), " ", ts1.value() + ts2.value() + ts3.value())
    time.sleep(1)
```
This code allowed me to see what each tilt switch was outputting, as well as the total that would be used to determine an output, this became a resource I would rely on when combining my Inputs and Outputs.

I ran into my first and probably most major issue of my project, my Liquid Mecrury Tilt Switchs became unreliable. The liquiid mercury tended to bounch when making such minute changes needed in my functional requirments, meaning I had to find an alternate. Although for a long time I thought it wasn't the sensors and when down a rabbit hole of interesting fixes.
1. The first thing I tried when trying to fix this issue, sadly was I created my favourite peice of code I made for this project:
```
    def stable_read(pin):
        samples = []
        for _ in range(5):
            samples.append(pin.value())
            time.sleep(0.002)
        return 1 if sum(samples) >= 3 else 0
```
I created a function which very quickly sampled the ON/OFF state of the Tilt Switches, and then if the result was a majority read ON, and a minority read OFF. I made this function in the hope that it would've fixed the bouncing issue, substituting in different samples and speeds It still didn't work and so I moved on to other fixes.

2. The second thing I tried was fixing my wiring, I started by spreading out the Tilt Switchs pins:
```
    ts1 = Pin(17, Pin.IN, Pin.PULL_DOWN)
    ts2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
    ts3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
```
I also wove the positive and negative wires out of the tilt switch to declutter them.
3. I also tried physically securing Tilt Switches to the level carboard, through tape to both remove altering orientation between tests, but also reduing shaking and vibrations that led to bouncing in the Tilt Switch.
4. None of the attampted soloutions seemed to work so finaly I changed to the other form of Tilt Switch we have access to, the Metal Ball Tilt Switchs work and worked much more effectively and efficiently then the Liquid Mercury Tilt Switches, by reducing the existing bouncing. The only downside with these Tilt Switches is the occasionally get stuck.
#### Evaluation
The process for my Tilt Switches was the longest test case process of this project, as I had to setup the Tilt Swtichs, and then deal with the problem that they barely worked. In the end I met most of my requirments, excluding there impact on Outputs which I will talk about in my next Test Case. When the liquid mercury switches became unreliable, I attempted several fixes including software stabilisation, rewiring, and physically securing the sensors, each allowing me a closer look at what the eventual soloution would be, taking out my existing hardware completely and replacing them. The most difficult part of this process was the fact that after quite a bit of code work, I would need to make a hardware change, and discard that work. An area of my code that could be improved, is substituting my placeholders with the now set up Tilt Switches.
### Test Case 4 - Combined Behaviour of System (Input and Output)
This Test Case is a combination of the Test Cases listed above in Requirments Outline including:
- Full System Combined Behaviour for >20° angle of system
- Full System Combined Behaviour for 10-20° angle of system 
- Full System Combined Behaviour for 5-10° angle of system
- Full System Combined Behaviour for 0-5° angle of system
As they are all simliar test cases relating to the same code.
#### Plan Outline
The following points are objectives that need to be adjusted in my prototype for my system to reach what is defined in my functional/non-functional requirments:
- Removal of placeholder values and integration of commputation
- Set up Tilt Switch Input to feed into computation
- Outputs (Buzzer and LEDs) feed from computed value.
#### Code Adjustment and Testing
The first thing I did was to try and get the Tilt Switches to have any effect over Outputs (Buzzer and LEDs), I did this by removing the old placeholder and substituting in the new way to find the angle range:
```
sensor1 = 0 #Placeholder values for coming tilt switches
sensor2 = 0
sensor3 = 0

ts = (sensor1 + sensor2 + sensor3)

|  Old
| 
V  New

ts = 0
ts = ts1.value() + ts2.value() + ts3.value()
```
#### Evaluation
++

++

++

++
Working Product Video -> Attached Seperately in the Google Classroom turn in

Thonny / VS Code files and folder structure -> Attached to Google Classroom turn in

Test Cases -> Attached above in PROJECT_DOCUMENTATION, "Testing and Debugging"

Commits -> Github history and below in PROJECT_DOCUMENTATION, "Github Commits"
# Evaluation
## Peer Evaluation
Plus, Minus, Implication
### PMI 1 - Lucas L 18/08/26
| Plus | Minus | Implication |
|---------- |---------- |----------------   |
| Program works very well and meets the requirement outline very well. The code functions perfectly and is highly efficient, without any excess code. The inclusion of external sensors is executed very well. The use of the buzzer and the different speeds it buzzes at as well as the combination of the different LED is used together seamlessly and is very satisfying to use.| The only issues with the program is the switches faces certain issues like it gets stuck at certain points, creating a small inconvenience. | In future, the system could be improved simply by implementing more efficient sensors. |
### PMI 2 - Max Edmunds - 22/08/26
| Plus | Minus | Implication |
|---------- |---------- |----------------   |
| An interesting idea, simple to code yet effective in purpose, it fulfills all of the functional requirements with neat code too. There is a distinct difference between the buzzers through their tempo and there are different coloured LEDs. Issue makes sense and there is a lot of work to support your need.
 | The system seems to be a little unreliable - the blue LED and fast pitched buzzer didn’t get alerted towards the end of the video. 
 | A well thought-out and intricately-designed structure that has a great need, strong solution and good difference. Things to improve on could be the non-functional requirements like reliability, and an additional idea to improve on the device would be to have a ‘Ding!’ effect at perfect level instead of a very fast buzzer that could get annoying |
## Self Evaluation
++

++

++

++

### Functional Criteria Evaluation
++

++

++

++

### Non-Functional Criteria Evaluation
++

++

++

++

### Performance for Identified Need Evaluation
++

++

++

++

### Project Management Evaulation
++

++

++

++

### Peer Evaluation Evaluation
++

++

++

++

### Future Impovments
++

++

++

++

# Github Commits (Replacement of Lacking Commits)