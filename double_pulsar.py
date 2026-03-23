from microbit import *

level1 = Image("00000:00300:03530:00300:00000")
level2 = Image("00300:03530:35753:03530:00300")
level3 = Image("03530:35753:57975:35753:03530")
level4 = Image("35753:57975:79997:57975:35753")
level5 = Image("57975:79997:99999:79997:57975")

pulsar = [level1, level2, level3, level4, level5, level4, level3, level2, level1]
flashing = [level1, level5, level1, level5, level1, level5, level1]

while True:
    for frame in pulsar:
        display.show(frame)
        sleep(200)
        
    sleep(400)
    
    for frame in pulsar:
        display.show(frame)
        sleep(80)
        
    sleep(400)
        
    for frame in flashing:
        display.show(frame)
        sleep(30)
        
    sleep(400)
    