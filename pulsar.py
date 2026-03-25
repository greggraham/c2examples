# Display a pulsing star image.

from microbit import *

level1 = Image("00000:00300:03530:00300:00000")
level2 = Image("00300:03530:35753:03530:00300")
level3 = Image("03530:35753:57975:35753:03530")
level4 = Image("35753:57975:79997:57975:35753")
level5 = Image("57975:79997:99999:79997:57975")

pulsar = [level1, level2, level3, level4, level5, level4, level3, level2]

display.show(pulsar, loop=True, delay=100)
