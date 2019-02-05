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
# TASK 4 --  Create Square frame
#---------------------------------

from MovingShapes import *

frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()


##--------------------------------
# TASK 5 --  Move Sqaure
#---------------------------------

shape1.moveTick(100, 40)