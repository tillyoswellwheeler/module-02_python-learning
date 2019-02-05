#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:23:32 2019

@author: matildaoswell-wheeler
"""

#---------------------------------
## CHAPTER 13 -- OOP Revision 
#---------------------------------

##--------------------------------
# TASK 1 --  First Moving Figure
#---------------------------------

from Shapes import *

frame = Frame()
s1 = Shape('square', 100)
s1.goto(200,100)

##--------------------------------
# TASK 2 --  More Obvious Movement
#---------------------------------
for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = x + 5
    
    x = 0
    y = 0
    