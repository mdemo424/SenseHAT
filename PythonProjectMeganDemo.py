from sense_hat import SenseHat
from time import sleep, strftime
from datetime import date
import calendar

my_date = date.today()
weekday = calendar.day_name[my_date.weekday()] 

sense = SenseHat()


# Colors

t = (100, 100, 0) #tan
r = (255, 0, 0) #red
o = (255, 165, 0) #orange
y = (255, 255, 0) #yellow
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
i = (75, 0, 130) #indigo (more purple)
v = (238, 130, 238) #violet (more pink)
n = (135, 80, 22) #brown
w = (255, 255, 255) #white
e = (0, 0, 0)  # e stands for empty/black


#Wreath

Day1 = [
    e,e,e,g,g,e,e,e,
    e,g,r,g,r,g,g,e,
    e,g,g,e,e,g,g,e,
    g,g,e,e,e,e,g,r,
    g,r,e,e,e,e,g,g,
    e,g,g,e,e,r,g,e,
    e,g,g,g,g,g,g,e,
    e,e,e,r,g,e,e,e
    ]
#Rudolph Reindeer

Day2 = [
    t,e,t,e,e,t,e,t,
    t,t,t,e,e,t,t,t,
    e,t,e,e,e,e,t,e,
    e,t,n,n,n,n,t,e,
    e,n,w,n,n,w,n,e,
    e,e,n,n,n,n,e,e,
    e,e,n,r,r,n,e,e,
    e,e,n,r,r,n,e,e
    ]

#Crhistmas Tree

Day3 = [
    e,e,e,g,g,e,e,e,
    e,e,g,r,g,g,e,e,
    e,e,g,g,g,b,e,e,
    e,g,b,g,r,g,g,e,
    e,g,g,g,g,b,g,e,
    g,b,g,r,g,g,r,g,
    e,e,e,n,n,e,e,e,
    e,e,e,n,n,e,e,e
    ]

#Candy Cane

Day4 = [
    e,e,w,r,r,w,e,e,
    e,r,w,w,r,w,w,e,
    e,r,r,e,e,w,r,e,
    e,e,e,e,w,r,r,e,
    e,e,e,r,w,w,e,e,
    e,e,w,r,r,e,e,e,
    e,r,w,w,e,e,e,e,
    e,r,r,e,e,e,e,e
    ]

#Present With Bow

Day5 = [
    e,e,r,e,e,r,e,e,
    e,e,r,r,r,r,e,e,
    e,e,r,r,r,r,e,e,
    e,g,g,r,r,g,g,e,
    e,g,g,r,r,g,g,e,
    e,r,r,r,r,r,r,e,
    e,g,g,r,r,g,g,e,
    e,g,g,r,r,g,g,e
    ]

#Santa With Hat

Day6 = [
    e,e,r,r,r,r,e,e,
    e,r,r,r,r,r,r,e,
    w,w,r,r,r,r,r,e,
    w,w,t,t,t,t,t,t,
    e,e,t,b,t,t,b,t,
    e,e,t,t,t,t,t,t,
    e,e,t,v,t,t,v,t,
    e,e,e,t,v,v,t,e
    ]

#Snowflake

Day7 = [
    w,e,w,e,e,w,e,w,
    e,b,e,e,e,e,b,e,
    w,e,b,b,b,b,e,w,
    e,e,b,w,w,b,e,e,
    e,e,b,w,w,b,e,e,
    w,e,b,b,b,b,e,w,
    e,b,e,e,e,e,b,e,
    w,e,w,e,e,w,e,w
    ]

sense.clear()
event = sense.stick.wait_for_event()

if event.action == "pressed" and event.direction == "middle":
    month = strftime("%B")
    if month == "December":
        if weekday == 'Sunday':
            sense.set_pixels(Day1)
        elif weekday == 'Monday':
            sense.set_pixels(Day2)
        elif weekday == 'Tuesday':
            sense.set_pixels(Day3)
        elif weekday == 'Wednesday':
            sense.set_pixels(Day4)
        elif weekday == 'Thursday':
            sense.set_pixels(Day5)
        elif weekday == 'Friday':
            sense.set_pixels(Day6)
        elif weekday == 'Saturday':
            sense.set_pixels(Day7)
    else:
        sense.show_message("Keep Waiting!")