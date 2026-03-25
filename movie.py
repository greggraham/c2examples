# A little movie.

from microbit import *

frame1 = Image("55055:50005:50505:50005:55055")
frame2 = Image("55055:50005:50505:50005:55955")
frame3 = Image("55055:50005:50505:50905:55055")
frame4 = Image("55055:50005:50505:59005:55055")
frame5 = Image("55055:50005:59505:50005:55055")
frame6 = Image("55055:59005:50505:50005:55055")
frame7 = Image("55055:50905:50505:50005:55055")
frame8 = Image("55955:50005:50505:50005:55055")

movie = [frame1, frame2, frame3, frame4,
         frame5, frame6, frame7, frame8, frame1]

display.show(movie, loop=True, delay=500)
