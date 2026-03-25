# Sleeps if you lay it down

from microbit import *

while True:
    acc_y = accelerometer.get_y()
    if acc_y < 500:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.HAPPY)