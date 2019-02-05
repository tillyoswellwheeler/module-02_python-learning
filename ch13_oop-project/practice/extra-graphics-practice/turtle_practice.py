#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:58:04 2019

@author: matildaoswell-wheeler
"""

import turtle
import math

#---------------------------------
## CHAPTER 13 -- Turtle practice
#---------------------------------

##--------------------------------
# TASK 1 --  Creating a square
#---------------------------------

#draw = turtle.Turtle()

#draw.color("cyan") #This colours the line being drawn
#draw.color("cyan", "blue") #The addition of a 2nd argument dictates the fill colour
#
#
#draw.begin_fill() # This creates a fill by using a begin and end around a shaoe
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.end_fill() # The fill ends here and effects everything between begin  and end
#
#draw.penup()
#draw.forward(100)
#draw.pendown()
#
#draw.begin_fill()
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.right(90)
#draw.forward(100)
#draw.end_fill()

##--------------------------------
# TASK 2 --  Creating a star
#---------------------------------

#draw.color("red", "cyan")
#draw.speed(10)
#
#draw.begin_fill()
#for star_draw in range(50):
#    draw.forward(200)
#    draw.right(170)
#draw.end_fill()

##--------------------------------
# TASK 3 --  Using math to create 
#---------------------------------

#draw.color("red", "cyan")
#draw.speed(10)
#
#draw.begin_fill()
#for star_draw in range(50):
#    draw.forward(math.sqrt(star_draw)*20)
#    draw.right(170)
#draw.end_fill()

##--------------------------------
# TASK 4 --  Creating stars 
#---------------------------------
star = turtle.Turtle()
star.getscreen().bgcolor("#994444") # Changes window colour and creates window

##--- Stage One              
#def star(star): # Creating a function that takes in one argument.
#    for star_draw in range(5): # Loop that runs through the turtle directions 5 times to get star shape.
#        star.forward(200)
#        star.left(216)

#--- Stage Two              
def star(turtle, size): # Using turle but you can use anything here. It is a placeholder.
    if size <= 10:
        return
    else:
        for star_draw in range(5): # Loop that runs through the turtle directions 5 times to get star shape.
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)             

star(turtle, 100) # Make sure to call the same placeholder as function.

turtle.done()