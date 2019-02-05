# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:45:35 2018

@author: 612383362
"""

#my_name = "Zed A. Shaw"
#my_age = 35 # not a lie
#my_height = 74
#my_weight = 180
#my_eyes = "Blue"
#my_teeth = "White"
#my_hair = "Brown"
#
#print("Let's talk about %s." % my_name)
#print("He's %d inches tall." % my_height)
#print("He's %d pounds heavy." % my_weight)
#print("Actually that's not too heavy.")
#print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
#print("His teeth are usually %s depending on the coffee." % my_teeth)
#
## Tricky line
#print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

### Chaning the variables assignments

name = "Zed A. Shaw"
age = 35 # not a lie
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# Tricky line
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

## Convert inches to cm

def inches_input():
    inches = int(input("Inches: "))
    convert_inches_to_cm(inches_input)


def convert_inches_to_cm(inches_input):
    print(inches_input *.round(2.54))   ### I can't work out this problem
    
inches_input()
    