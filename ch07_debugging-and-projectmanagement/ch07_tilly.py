# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:36:08 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER SEVEN - Debugging
#---------------------------------------------------------------------------------------

############################################
# Task 1 - Creating errors to find and fix

userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result

def nestedOperation(result):
    = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

###########################################
# Steps to debug a program

# 1. Three sets of buttons in on the top row are some blue buttons. These buttons are the debugging buttons.
# 2. To start the debugging click on the blue play/pause button.
# 3. Use the next three buttons to do staggered line by line analysis.
# 4. Stop the debugging with the stop button.