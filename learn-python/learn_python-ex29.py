# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:45:17 2018

@tillyoswellwheeler: 612383362
"""

### Original script

#people = 20
#cats = 30
#dogs = 15
#
#
#if people < cats:
#    print("Too many cats! The world is doomed!")
#
#if people > cats:
#    print("Not many cats! The world is saved!")
#
#if people < dogs:
#    print("The world is drooled on!")
#
#if people > dogs:
#    print("The world is dry!")
#
#
#dogs += 5
#
#if people >= dogs:
#    print("People are greater than or equal to dogs.")
#
#if people <= dogs:
#    print("People are less than or equal to dogs.")
#
#
#if people == dogs:
#    print("People are dogs.")
    
### Change it to a function
    
people = 20
cats = 30
dogs = 15

def more_cats_than_people(cats, people):
    
    if people < cats:
        print("Too many cats! The world is doomed!")
    
    elif people > cats:
        print("Not many cats! The world is saved!")
    else:
        print("Just right!")
    
def more_dogs_than_people(dogs, people):
    
    if people < dogs:
        print("The world is drooled on!")
    if people > dogs:
        print("The world is dry!")
    else:
        print("Just right!")    


more_dogs_than_people(dogs, people)

more_cats_than_people(cats, people)


## Add 5 more dogs

#more_dogs_than_people(dogs + 5, people)
#    if people >= dogs:
#        print("People are greater than or equal to dogs.")
#    elif people <= dogs:
#        print("People are less than or equal to dogs.")
#    elif people == dogs:
#        print("People are dogs.")
#    else:
#        # Nothing to return.
        


