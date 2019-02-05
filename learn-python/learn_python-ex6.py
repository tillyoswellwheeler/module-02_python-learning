# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:18:54 2018

@author: 612383362
"""

x = "There are %d types of people" % 10 #Formatting a decimal number into a string
binary = "binary" # Assigning a string to a variable
do_not = "don't" "binary" # Assigning a string to a variable
y = "Those who know %s and those who %s." % (binary, do_not) #Formatting a string into a string

print(x)
print(y)

print("I said: %r." % x) # Presenting raw data to the user, in this instance it is being used to show the data assigned to the x variable.
print("I also said: '%s'." % y) # Formatting the y variable as a string into the string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # A space for the inputting of a variable

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)  # Printing two sets of string data and adding them together.