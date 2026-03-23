# Roll a die

from microbit import *
from random import choice

d1 = Image("00000:00000:00900:00000:00000")
d2 = Image("00000:00090:00000:09000:00000")
d3 = Image("00000:00090:00900:09000:00000")
d4 = Image("00000:09090:00000:09090:00000")
d5 = Image("00000:09090:00900:09090:00000")
d6 = Image("00000:09090:09090:09090:00000")

images = [d1, d2, d3, d4, d5, d6]

while True:
    # Do nothing while waiting for button a to be pressed
    while not button_a.was_pressed():
        pass
    
    # Display random die faces while waiting for button a to be pressed
    while not button_a.was_pressed():
        display.show(choice(images))
        sleep(10)
