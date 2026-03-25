from microbit import *
while True:
    temp_c = temperature()
    temp_f = int(temp_c * 9 / 5 + 32.5)
    display.scroll(str(temp_c) + " C - " + str(temp_f) + " F - ")
