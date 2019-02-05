# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:59:52 2018

@tillyoswellwheeler: 612383362
"""

def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTION %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")

########
## Returning things

def age_value(num1, num2):
    age = num1 + num2
    return age

print(age_value(30, 20))

########
##Normal formula for the puzzle

what = age + (height - (weight * (iq / 2)))

print("That becomes: ", what, "That's right!")

# The modified puzzle

what = age + (height + (weight * (iq / 2)))

print("That now becomes: ", what)

# Simple formula with numbers and functions

#add = 24 + 34 / 100 -1023

print(((24 + 34) / 100) - 1023)

simple_formula = subtract(divide(add(24, 34), 100), 1023)

print("That becomes: ", simple_formula, "That's right!")