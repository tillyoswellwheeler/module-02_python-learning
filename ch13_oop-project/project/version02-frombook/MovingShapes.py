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
# TASK 3 --  Define classes
#---------------------------------

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.x = x(0)
#        self.y = y(0)
#        self.dx = dx(0)
#        self.dy = dy(0)
    def goto(self, x, y):
        self.figure.goto(x, y)
    def moveTick(self, forward, left):
        turtle.forward(0)
        turtle.left(0)
        
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)

class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)

class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
