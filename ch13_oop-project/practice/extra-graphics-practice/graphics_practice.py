#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:44:52 2019

@author: matildaoswell-wheeler
"""

#------------------------------------------
## CHAPTER 13 -- Computer Graphics practice
#------------------------------------------

##-----------------------------------
# TASK 1 --  Creating different shape
#------------------------------------

from tkinter import *
import random
import time

#tk = Tk()
#canvas = Canvas(tk, width=500, height=400)
#tk.title("Drawing")
#canvas.pack()
#
#canvas.create_line(0, 0, 500, 400)
#canvas.create_rectangle(100, 100, 250, 150, fill="blue")
#canvas.create_oval(10, 10, 250, 250, fill="green")
#canvas.create_oval(10, 10, 150, 300, fill="orange")
#canvas.create_polygon(10, 100, 100, 300, 500, 300, fill="blue")
#
#canvas.mainloop()

##-----------------------------------
# TASK 2 --  Animating simple shapes
#------------------------------------

#WIDTH = 800 # Constants -- indicate to everyone that these arent changeable values
#HEIGHT = 600
#
#tk = Tk()
#canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
#tk.title("Drawing")
#canvas.pack()
#
#ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
#xspeed = 1 # Adding variables to make dry code
#yspeed = 5 # Adding variables to make dry code
#
## This code below moves the drawn circle 1px for a range of 400 times.
##for i in range(400):
##    canvas.move(ball, 1, 0)
##    tk.update()
##    time.sleep(0.01)
#
## Now we use a while loop
#while True:
#    canvas.move(ball, xspeed, yspeed) # We add in the new xspeed and yspeed variables
#    pos = canvas.coords(ball)
#    if pos[3] >= HEIGHT or pos[1] <= 0: # This is using the array list of the canvas and the coords to stop the ball.
#        yspeed = -yspeed 
#    if pos[2] >= WIDTH or pos[0] <=0:
#        xspeed = -xspeed
#    tk.update()
#    time.sleep(0.01)
#
#canvas.mainloop()

##-----------------------------------
# TASK 3 --  Animating with Objects
#------------------------------------

#WIDTH = 800 # Constants -- indicate to everyone that these arent changeable values
#HEIGHT = 600
#
#tk = Tk()
#canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
#tk.title("Drawing")
#canvas.pack()
#
#class Ball:
#    def __init__(self, colour, size): # Adding new arguments that we then use in the method below.
#        self.shape = canvas.create_oval(10, 10, size, size, fill=colour)
#        self.xspeed = random.randrange(1,8) # Adding random speed to the y and x positions
#        self.yspeed = random.randrange(1,8) 
#        
#    def move(self):
#        canvas.move(self.shape, self.xspeed, self.yspeed) 
#        pos = canvas.coords(self.shape)
#        if pos[3] >= HEIGHT or pos[1] <= 0: 
#            self.yspeed = -self.yspeed 
#        if pos[2] >= WIDTH or pos[0] <=0:
#            self.xspeed = -self.xspeed
#
#newball = Ball("red", 50) # You just need one value because they are its diameter really.
#newball2 = Ball("orange", 100)
#
#while True:
#    newball.move()
#    newball2.move()
#    tk.update()
#    time.sleep(0.01)
#
#canvas.mainloop()

##--------------------------------------
# TASK 4 --  More animating with Objects
#---------------------------------------

# Adding unlimited amount of balls with random movements, size and colour
WIDTH = 800 # Constants -- indicate to everyone that these arent changeable values
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

class Ball:
    def __init__(self, colour, size): # Adding new arguments that we then use in the method below.
        self.shape = canvas.create_oval(10, 10, size, size, fill=colour)
        self.xspeed = random.randrange(-10,10) # Using minus makes it go left as well as right.
        self.yspeed = random.randrange(-10,10) 
        
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed) 
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0: 
            self.yspeed = -self.yspeed 
        if pos[2] >= WIDTH or pos[0] <=0:
            self.xspeed = -self.xspeed
            
# The list below is full of colours. The random.choice(colours) uses this list and selects from it at random.
colours = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta', 'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

balls = [] # Creates an empty list
for i in range(100):
#    balls.append(Ball("red", 50)) # This uses the append function to create and add a ball to the empty ball list.
    balls.append(Ball(random.choice(colours), random.randrange(50, 100))) # This uses range to create a range of sizes.

while True:
    for ball in balls: # We loop through the balls list and use the placeholder ball.
        ball.move() # Here we use the ball and move it with the move function
    tk.update()
    time.sleep(0.01)

canvas.mainloop()