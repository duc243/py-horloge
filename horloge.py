# coding=utf-8

import turtle
from datetime import *

# Lift the paintbrush and move it forward for a distance
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()

def mkHand(name, length):
    # Register the Turtle shape and create the hand Turtle
    turtle.reset()
    Skip(-length * 0.1)
    # Start recording the vertices of the polygon. The current turtle position is the first vertex of the polygon.
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # Stop recording the vertices of the polygon. The current turtle position is the last vertex of the polygon. Will be connected to the first vertex.
    turtle.end_poly()
    # Return the last recorded polygon.
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)
