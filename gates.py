from microbit import *
from random import randint

x = randint(0, 4)
y = 4
sleep_time = 20
speed = 2  # moves per second
move_count_amount = (1000 / speed) / sleep_time
move_counter = move_count_amount
gate_x = randint(0, 4)
gate_count = 0
while True:
    
    # Calculate movements
    if button_a.was_pressed():
        x -= 1
        if x < 0:
            x = 0
    if button_b.was_pressed():
        x += 1
        if x > 4:
            x = 4
    
    if move_counter <= 0:
        y -= 1
        if y <= 0:
            if x != gate_x:
                display.scroll("Crash! " + str(gate_count) + " gates")
                break
            else:
                y = 4
                x = randint(0, 4)
                gate_x = randint(0, 4)
                gate_count += 1
        move_counter = move_count_amount
    
    # Draw display
    display.clear()
    for dx in range(0, 5):
        if dx == gate_x:
            display.set_pixel(dx, 0, 0)
        else:
            display.set_pixel(dx, 0, 9)
    
    display.set_pixel(x, y, 9)
    
    move_counter -= 1
    sleep(sleep_time)
