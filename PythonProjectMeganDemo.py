from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours


r = (255, 0, 0)
o = (255, 165, 0)
y = (255, 255, 0)
g = (0, 128, 0)
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