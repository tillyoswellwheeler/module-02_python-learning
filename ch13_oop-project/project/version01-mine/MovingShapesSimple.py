#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:23:32 2019

@author: matildaoswell-wheeler
"""

#---------------------------------
## CHAPTER 13 -- OOP Project
#---------------------------------

##--------------------------------
# TASK 1 --  Define classes
#---------------------------------

WIDTH = 800 # Constants -- indicate to everyone that these arent changeable values
HEIGHT = 600

from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

class MovingShape:
    def __init__(self, colour, size, start_position): 
        self.xspeed = random.randrange(-10,10) # Using minus makes it go left as well as right.
        self.yspeed = random.randrange(-10,10)
        self.start_position = canvas.cords(self.shape).random.randrange( # Attempting to randomise the start position
        
        # Add in True and False
        
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed) 
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0: 
            self.yspeed = -self.yspeed 
        if pos[2] >= WIDTH or pos[0] <=0:
            self.xspeed = -self.xspeed

    
class Square(MovingShape):
    def __init__(self, colour, size): # Adding new arguments that we then use in the method below.
        MovingShape.__init__(self, colour, size)
        self.shape = canvas.create_rectangle(10, 10, size, size, fill=colour)
        self.xspeed = random.randrange(-10,10) # Using minus makes it go left as well as right.
        self.yspeed = random.randrange(-10,10) 

#class Diamond(MovingShape):
#    def __init__(self, colour, size): # Adding new arguments that we then use in the method below.
#        self.shape = (canvas.create_rectangle(10, 10, size, size, fill=colour)) t.tilt(45)
#        self.xspeed = random.randrange(-10,10) # Using minus makes it go left as well as right.
#        self.yspeed = random.randrange(-10,10)    


class Circle(MovingShape):
    def __init__(self, colour, size): # Adding new arguments that we then use in the method below.
        self.shape = canvas.create_oval(10, 10, size, size, fill=colour)
        self.xspeed = random.randrange(-20,20) # Using minus makes it go left as well as right.
        self.yspeed = random.randrange(-20,20)    

        
            



