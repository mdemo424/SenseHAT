from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

t = (100, 100, 0)
r = (255, 0, 0)
o = (255, 165, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (238, 130, 238)
n = (135, 80, 22)
w = (255, 255, 255)
e = (0, 0, 0)  # e stands for empty/black


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

sense.set_pixels(Day5)
