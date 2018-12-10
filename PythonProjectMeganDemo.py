from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {

  'r' : [255, 0, 0],
  'o' : [255, 165, 0]
  'y' : [255, 255, 0]
  'g' : [0, 128, 0]
  'b' : [0, 0, 255]
  'i' : [75, 0, 130]
  'v' : [238, 130, 238]
  'n' : [135, 80, 22],
  'w' : [255, 255, 255],
  'e' : [0, 0, 0]  # e stands for empty/black

}

# Pictures
e,e,e,r,r,e,e,e,e,e,r,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,r,e,e,e,e
e,g,g,e,e,g,g,e,e,e,g,r,r,g,e,e,e,e,w,w,w,w,e,e,e,w,n,w,n,n,w,e,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,e,n,n,n,n,n,n,e,e,e,n,n,n,n,e,e
e,e,e,v,v,e,e,e,e,e,e,v,v,e,e,e,e,e,v,y,v,y,e,e,e,v,y,v,y,v,y,e,e,y,v,y,v,y,v,e,e,v,y,v,y,v,y,e,e,y,v,y,v,y,v,e,e,e,y,v,y,v,e,e
e,e,e,g,g,g,e,e,e,e,g,g,g,e,g,e,e,w,w,w,w,w,e,w,n,n,b,n,b,n,n,e,e,n,n,n,n,n,e,e,e,n,n,v,n,n,e,e,e,e,n,n,n,e,e,e,e,g,g,g,g,g,e,e
e,e,g,e,e,e,e,e,e,e,g,g,e,e,e,e,e,g,g,e,e,e,e,g,e,e,g,g,e,g,g,g,e,g,g,e,g,g,g,e,e,e,g,g,g,g,g,e,e,e,r,r,g,e,e,e,e,e,r,r,e,e,e,e
e,e,e,g,g,e,e,e,e,e,g,i,g,g,e,e,e,g,g,g,g,g,g,e,e,e,g,g,g,g,e,e,e,g,g,g,g,i,g,e,g,g,i,g,g,g,g,g,e,e,e,o,o,e,e,e,e,e,e,o,o,e,e,e
e,e,e,r,r,r,e,e,e,e,r,r,r,e,r,e,e,w,w,w,w,w,e,w,e,n,b,n,b,n,e,e,e,n,n,w,n,n,e,e,e,n,w,v,w,n,e,e,e,e,w,w,w,e,e,e,e,r,r,r,r,r,e,e
e,e,e,e,e,w,r,e,e,e,e,e,r,e,e,w,e,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e
e,i,e,e,e,e,e,e,i,i,e,i,e,e,e,e,e,e,i,o,i,e,e,e,e,i,o,i,o,i,e,e,e,e,i,o,i,o,i,e,e,e,e,i,o,i,e,e,e,e,e,e,i,e,i,i,e,e,e,e,e,e,i,e
e,e,e,e,y,e,e,e,e,e,y,y,y,y,y,e,e,e,e,y,y,y,e,e,e,e,e,y,e,y,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,i,e,i,e,i,e,e,n,n,n,n,n,n,n,n
w,e,w,w,w,e,w,e,e,w,e,w,e,w,e,e,w,e,w,w,w,e,w,e,w,w,w,w,w,w,w,e,w,e,w,w,w,e,w,e,e,w,e,w,e,w,e,e,w,e,w,w,w,e,w,e,e,e,e,e,e,e,e,e
e,g,e,e,e,e,g,e,e,e,g,g,g,g,e,e,e,r,r,g,g,r,r,e,e,r,r,g,g,r,r,e,e,g,g,g,g,g,g,e,e,g,g,g,g,g,g,e,e,r,r,g,g,r,r,e,e,r,r,g,g,r,r,e
e,e,e,o,e,e,e,e,e,e,e,o,y,e,e,e,e,e,e,e,o,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e
n,n,e,e,e,e,n,n,e,n,e,e,e,e,n,e,e,n,n,e,e,n,n,e,e,e,n,n,n,n,e,e,e,e,n,i,i,n,e,e,e,e,n,n,n,n,e,e,e,e,n,n,n,n,e,e,e,e,e,r,r,e,e,e
e,e,e,g,e,e,e,e,e,e,g,e,g,e,e,e,e,e,g,e,e,g,e,e,e,g,e,e,e,g,e,e,e,w,e,e,e,e,g,e,e,w,w,e,e,g,w,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e,e
e,e,n,n,e,e,e,e,e,n,i,n,e,e,e,e,o,w,n,n,n,e,e,e,e,w,n,n,n,n,e,e,e,r,r,n,n,n,e,e,e,e,r,r,n,n,n,n,e,e,o,e,r,e,n,n,e,o,e,o,e,e,e,e
e,e,e,g,g,g,g,e,e,e,g,g,g,g,e,w,e,r,r,r,r,r,r,e,e,e,w,w,w,w,e,e,e,w,i,w,i,w,w,e,e,w,w,o,w,w,w,e,e,e,w,w,w,w,e,e,e,e,e,w,w,e,e,e
e,e,e,e,e,e,e,e,e,e,g,e,e,g,e,e,g,e,g,g,e,g,e,e,e,g,g,g,g,g,g,g,e,g,g,g,g,g,g,e,e,g,n,n,n,n,g,e,n,n,i,n,i,n,n,n,e,n,n,n,n,n,n,e
e,e,e,e,e,e,e,e,e,e,e,e,e,e,y,v,e,e,e,e,e,g,b,i,e,e,e,r,r,r,r,r,e,r,r,r,r,r,r,r,e,e,r,r,r,r,r,r,y,e,r,e,e,e,r,e,e,y,y,y,y,y,y,y
e,e,y,y,y,y,e,e,e,e,e,n,n,e,e,e,e,e,e,n,n,e,e,e,e,y,y,w,w,y,y,e,e,e,y,w,w,y,e,e,e,e,e,w,w,e,e,e,e,e,w,w,w,w,e,e,e,w,w,w,w,w,w,e
e,e,e,e,e,e,e,e,e,g,g,e,e,g,g,e,e,e,g,g,g,g,e,e,e,e,y,r,r,y,e,e,y,y,y,y,y,y,y,y,y,y,y,e,e,y,y,y,e,y,y,e,e,y,y,e,e,e,e,e,e,e,e,e
e,n,n,e,n,n,e,e,e,e,n,e,n,e,e,e,e,w,w,w,w,w,w,e,e,o,o,o,w,w,o,e,e,w,w,o,o,o,o,e,e,o,o,o,o,o,o,e,e,o,o,o,w,w,w,e,e,o,o,o,w,o,o,e
e,e,r,g,g,g,e,e,e,g,g,e,r,g,g,e,g,g,e,e,e,e,g,g,g,r,e,e,e,e,r,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,r,e,r,g,e,e,g,g,e,e,e,g,g,r,g,e,e
e,e,e,n,e,e,e,e,e,e,e,n,n,e,n,e,e,e,e,n,e,e,n,n,e,e,e,n,e,n,e,e,e,e,n,n,n,n,e,e,n,n,n,n,n,n,n,e,n,n,n,n,n,n,n,e,e,n,n,n,n,n,e,e
e,e,e,w,w,w,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,r,r,r,r,r,e,e,r,r,r,r,r,e,e,e,e,e,r,r,e,e,e,e

# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
# Display a given picture string on the sense HAT
# ------------------------------------------------
def display_pic(pic_string):

  # Get rid of newline and split the line into a list
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  # Look up each letter in the dictionary of colours and add it to the list
  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])

  # Display the pixel colours from the file
  sense.set_pixels(pic_list)



# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------