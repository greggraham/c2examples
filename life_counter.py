from microbit import *
import random

life = 20
timer = 0
timeout = 7000

while life > 0:
    if button_a.was_pressed():
        life -= 1
        timer = 0
    elif button_b.was_pressed():
        life += 1
        timer = 0
    elif accelerometer.was_gesture("up"):
        display.scroll(str(life))
        timer = 0
    elif timer > timeout:
        display.scroll(str(life))
        timer = 0
    else:
        timer += 1

for i in range(3):
    display.scroll("Game Over")

