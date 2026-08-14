import machine
import time
from machine import Pin

ts1 = Pin(17, Pin.IN, Pin.PULL_DOWN)
ts2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
ts3 = Pin(20, Pin.IN, Pin.PULL_DOWN)

def stable_read(pin):
    samples = []
    for _ in range(5):          # take 5 quick samples
        samples.append(pin.value())
        time.sleep(0.002)       # 2ms between samples
    return 1 if sum(samples) >= 3 else 0   # majority vote

while True:
    sts1 = stable_read(ts1)
    sts2 = stable_read(ts2)
    sts3 = stable_read(ts3)

    print(sts1, sts2, sts3, sts1 + sts2 + sts3)
    time.sleep(1)
