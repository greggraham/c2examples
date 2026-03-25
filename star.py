# Display a star image.

from microbit import *

star = Image("03530:35753:57975:35753:03530")

while True:
    if button_a.is_pressed():
        display.show(star)
    else:
        display.clear()
