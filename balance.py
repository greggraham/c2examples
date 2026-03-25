# Ball balancer

from microbit import *

xf = 0.0
yf = 0.0
old_x = 0
old_y = 0
x = 0
y = 0
rate = 0.02
rate_incr = 0.005

display.clear()

while True:
    if button_a.was_pressed():
        rate -= rate_incr
    elif button_b.was_pressed():
        rate += rate_incr

    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 20 and xf < 4.0:
        xf += rate
    elif reading_x < -20 and xf > 0.0:
        xf -= rate
    if reading_y > 20 and yf < 4.0:
        yf += rate
    elif reading_y < -20 and yf > 0.0:
        yf -= rate
    x = int(xf)
    y = int(yf)
    if x != old_x or y != old_y:
        display.clear()
        old_x = x
        old_y = y
    display.set_pixel(x, y, 9)
