# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:51:06 2018

@author: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER TWO - Introduction to calculations, printing variables and string munipulation.
#---------------------------------------------------------------------------------------

#######################
# Printing calculations

print(5-6)
print(8 *9)
print(6 / 2)
print(5 / 2)
print(5.0 / 2)
print(5 % 2)
print(2 * (10 +3))
print(2 ** 4)

#######################
# Introduce Variables

x = 12.5
y = 3 * x + 2
#x = x + 1.1 # reassigning x variable


print(x)
print(y)

#######################
# String Operations

print('hello' + 'world')
print("Joke" * 3)
# print("Chen" + 3) invalid operation can't add an int to a string
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the ring".title())

#######################
# String Formatting

# .format(variable_0, variable_1, etc) 
# age_description = "My age is {0} and I like {1}.".format(age,like)

# Define the variable
age = 5
like = "painting"

age_description = "My age is {} and I like {}.".format(age,like)

print(age_description) 