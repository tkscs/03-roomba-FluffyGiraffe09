# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Orli <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here
for i in range(4):
    forward(40)
    right(90)
    forward(40*3)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(40*3)
    right(90)
    forward(40)
    left(180)
forward(40*2)
right(90)
for i in range(4):
    forward(40*2)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(40*2)
left(90)
forward(40)
right(90)
for i in range(4):
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(40)
left(90)
forward(40*3)
backward(40)
right(90)
forward(40)
backward(40*10)
for i in range(4):
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    right(180)
forward(40*2)
# End your code here
###
 
window.exitonclick()