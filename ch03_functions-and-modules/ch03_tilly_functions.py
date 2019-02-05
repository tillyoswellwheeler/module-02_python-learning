# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:05 2018

@author: 
"""

#---------------------------------------------------------------------------------------
# CHAPTER THREE - Functions, returning values and importing modules
#---------------------------------------------------------------------------------------

############################################
# Using variables and arguments

def hello_world_4args(a, b, c, d):
    print("{} {} {} {}".format(a, b, c, d))

##############################################
# First Function

def hello_world():
    print("Hello World!")

# Printing my name
def my_name():
    print("Tilly")

# Amend hello_world() by adding an extra functionality
def hello_world():
    print("Hello World!")
    print(2 + 2)    

# Functions and Arguments
def hello_world_2args(a,b):
    print ("{} {}".format(a,b))

# Making the above more collateral and Python by putting everything locally

def user_inputs():
    first_number_input = int(input("What's your first number to add? "))
    second_number_input = int(input("What's your second number to add? "))
    add_two_input_numbers(first_number_input, second_number_input)

def add_two_input_numbers(first_number_input, second_number_input):
    print(first_number_input + second_number_input)
    
############################################################
# Mid-Class Challenge -- Converting distance

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print("Converting distance in miles to kilometers.")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)

############################################################
# Mid-Class Challenge -- Converting temperature

def convert_temperture_kelvin(centigrade):
    kelvin = centigrade + 273.15
    print("Converting temperature in centigrade to kelvin.")
    print("Temperature in centigrade:", centigrade)
    print("Temperature in kelvin:", kelvin)
    

def convert_temperture_fahrenheit(centigrade):
    fahrenheit = (centigrade * 9.0) / 5.0 + 32
    print("Converting temperature in centigrade to fahrenheit.")
    print("Temperature in centigrade:", centigrade)
    print("Temperature in fahrenheit:", fahrenheit)

# Seperate function -- comment out the aove to use

centigrade1 = 12

def convert_temperture_kelvin(centigrade):
    kelvin = centigrade + 273.15
    
    return kelvin

def convert_temperture_fahrenheit(centigrade):
    fahrenheit = (centigrade * 9.0) / 5.0 + 32
    
    return fahrenheit

def convert_temperature_kelvin_to_fahrenheit(centigrade):
    kelvin1 =convert_temperture_kelvin(centigrade1)
    fahrenheit = ((kelvin1 * 9) / 5) - 459.67
    
    print("Converting temperature in kelvin to fahrenheit.")
    print("Temperature in kelvin:", kelvin1)
    print("Temperature in fahrenheit:", fahrenheit)
  