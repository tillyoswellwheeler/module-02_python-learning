#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:14:03 2019

@author: matildaoswell-wheeler
"""

#---------------------------------
## CHAPTER 13 -- OOP Project
#---------------------------------

##--------------------------------
# SET UP
#---------------------------------

WIDTH = 800 # Constants -- indicate to everyone that these arent changeable values
HEIGHT = 600

from tkinter import *
import random
import time
from MovingShapesSimple import *

##--------------------------------------
# TEST
#---------------------------------------


# The list below is full of colours. The random.choice(colours) uses this list and selects from it at random.
colours = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta', 'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']
#


    

shapes = []

#while True:
#    for shape in shapes: 
#        shape.move() 
#    tk.update()
#    time.sleep(0.01)
  
# Allows repeated shapes to appear  
for i in range(200):
#    shapes.append(Square("green", 60))
#    shapes.append(Circle("green", 30))
    shapes.append(Circle(random.choice(colours), random.randrange(50, 100))) 
    shapes.append(Square(random.choice(colours), random.randrange(50, 100))) 

for i in range(400):
    for shape in shapes:
        shape.move()
    tk.update() # Allows animation
    time.sleep(0.01)

canvas.mainloop()