# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:05 2018

@author: 
"""

#---------------------------------------------------------------------------------------
# CHAPTER THREE - Functions, returning values and importing modules
#---------------------------------------------------------------------------------------

###########################################
# User Input

print("What's your name?")
name = input()

#name = input("What's your name? ")

#print("Hello {}!".format(name))


print(("Hello {}!".format(name)).upper())

############################################
# Using variables and arguments

def hello_world_4args(a, b, c, d):
    print("{} {} {} {}".format(a, b, c, d))
    
a = "hello"
b = "world"
c = "you"
d = "know"
hello_world_4args(a, b, c, d)

##############################################
# First Function

def hello_world():
    print("Hello World!")

hello_world()


# Printing my name
def my_name():
    print("Tilly")

my_name()

# Amend hello_world() by adding an extra functionality
def hello_world():
    print("Hello World!")
    print(2 + 2)    

hello_world()

# Functions and Arguments
a1 = "hello"
b1 = "world"
a2 = "love"
b2 = "coding"

def hello_world_2args(a,b):
    print ("{} {}".format(a,b))
    
hello_world_2args(a1, b1)
hello_world_2args(a2,b2)
# Some functions can take more than one argument, and it will depend on what you need it to do.

first_number = 4
second_number = 5
#
#def add_two_numbers(first_number, second_number):  
#    print(first_number + second_number)
#
#add_two_numbers(first_number, second_number)

# User input numbers
#    
#first_number_input = int(input("What's your first number to add? "))
#second_number_input = int(input("What's your second number to add?"))
#
#def add_two_input_numbers(first_number_input, second_number_input):
#    print(first_number_input + second_number_input)
#    
#add_two_input_numbers(first_number_input, second_number_input)

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

convert_distance(44)

############################################################
# Mid-Class Challenge -- Converting temperature

def convert_temperture_kelvin(centigrade):
    kelvin = centigrade + 273.15
    print("Converting temperature in centigrade to kelvin.")
    print("Temperature in centigrade:", centigrade)
    print("Temperature in kelvin:", kelvin)
    

convert_temperture_kelvin(100)

def convert_temperture_fahrenheit(centigrade):
    fahrenheit = (centigrade * 9.0) / 5.0 + 32
    print("Converting temperature in centigrade to fahrenheit.")
    print("Temperature in centigrade:", centigrade)
    print("Temperature in fahrenheit:", fahrenheit)

convert_temperture_fahrenheit(34)

##
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
    
convert_temperature_kelvin_to_fahrenheit(centigrade1)
    