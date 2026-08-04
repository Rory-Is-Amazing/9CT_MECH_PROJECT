# Requirements Outline
### The Need 
In industries such as construction, production, engineering, and trades are often required to use abseloute precision. Precision is required due to even the smallest error can disrupt a larger picture. Similar tools exist for this role, such as levels which use two liquids to present the angle, there is need for a tool to do more than a basic level.
### Proposed Soloution
I will design an eletronic level, which through use of a set of LED lights, a buzzer and multiple Tilt Switchs will provide more detail to an individual using it. A row of led lights lined up in an order to depcit the accuracy of the level (ligth order: red, yellow, green, blue), as well as a buzzer which further away from flat buzzes faster, moving closer to accuraucy bring the buzzer to a slower buzz.

### Key Actions
1. Tilt switchs register the orientation of the device once every 0.1 second
2. Leds light up depending on orientation of device
3. Buzzer buzzs on proximity to flat orientation
### Functional Requirments
**LED Output**: Blue LED must light up if orientation is flat, Green LED if 2 of 3 Tilt Switches are on, Yellow LED if 1 of 3 Tilt Switches are on, and Red LED if no Tilt Switches are on.

**Buzzer**: Buzzer must read the amount of Tilt Switches on, and output the associatd beep speed, the more switches on the faster the beeps.

**Tilt Switchs**: Provide orientation of device once every 0.1 seconds.
### Test Case
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| <5° angle of device | 3/3 Tilt Switches On | Blue LED on, fastest Buzzer |
| >5° angle of device | 2/3 Tilt Switches On| Green LED on, faster Buzzer |
| >10° angle of device | 1/3 Tilt Switches On | Yellow LED on, slower Buzzer|
| >20° angle of device | 0/3 Tilt Switches On | Red LED on, slowest Buzzer|
### Non-Functional Requirments
**Efficiency** - My device is required to operate its function efficienly, through use of optemsied code.

**Response Time** - My device is to take input every ≈0.1 seconds, and outputing immediatly

**Accuracy** - My devices input accuracy will be composd of my combined sensors which will be able to detect changes at 5° intervals 


# Design
### Flow Chart
![Image](Image.png)
### Pseudo Code

```
BEGIN
    WHILE true
        READ switchs_on
        If switchs_on == 3 THEN
            red()
        ELSE IF switchs_on == 2 THEN
            yellow()
        ELSE IF switchs_on == 1 THEN
            green()
        ELSE IF switchs_on == 0 THEN
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

# Testing and Debugging

# Evaluation
