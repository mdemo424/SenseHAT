from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours

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



# Pictures
with open ("pictures.txt", "r") as f:
    all_pics = f.readlines()
door = all_pics[0]
# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
# Display a given picture string on the sense HAT
# ------------------------------------------------
def display_pic(pic_string):

  # Get rid of newline and split the line into a list
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

 

day = int(strftime("%d"))
month = strftime("%B")
whole_date = strftime("%d/%m/%y")
full_datetime = strftime("%d/%m/%y at %I:%M%p")

# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
while True:
    sense.clear()
    display_pic(door)
    event = sense.stick.wait_for_event()
    if event.action == "pressed" and event.direction == "middle":
        today = int(strftime("%d"))
        month = strftime("%B")
        if month == "December" and day < 25:
            sense.show_message(str(19-day) + " days left until winter break!", text_colour = 'v', back_colour = 'y', scroll_speed = 0.05)
            display_pic(all_pics[day])
            sleep(5)
        else:
            sense.show_message("Keep waiting")
            
            
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
Day3 = [
    e,e,e,g,g,e,e,e,
    e,e,g,g,g,g,e,e,
    e,e,g,g,g,g,e,e,
    e,g,g,g,g,g,g,e,
    e,g,g,g,g,g,g,e,
    g,g,g,g,g,g,g,g,
    e,e,e,n,n,e,e,e,
    e,e,e,n,n,e,e,e
    ]
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