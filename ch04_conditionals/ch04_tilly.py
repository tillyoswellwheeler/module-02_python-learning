# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:03:16 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER FOUR - Conditionals
#---------------------------------------------------------------------------------------

###########################################
# 

def teen_is_age(age):
    return age >= 13 and age <= 19

print(teen_is_age(15))
print(teen_is_age(22))

###### Task 3

num = int(input("Enter a number between 1 - 10: "))

def numbers_inbetween_1_and_10(num):
    if  0 < num <= 10:
        print("Just right!")
    elif num < 0:
        print("Too Low!")
    elif num > 10:
        print("Too high!")
    else:
        print("Don't know!")
        

numbers_inbetween_1_and_10(num) 

#### Task 4 - Order must stay the same to keep the logic working

age = int(input("How old are you? "))


def your_demographic(age):
    if age < 13:
        print("Child")
    elif age < 18:
        print("Teen")
    elif age < 65:
        print("Adult")
    else:
        print("Pensioner")    
        
your_demographic(age)

   


