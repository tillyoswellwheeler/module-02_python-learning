# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:37:18 2018

@author: tilly.oswellwheeler
"""

#---------------------------------------------------------------------------------------
# CHAPTER SIX - Using sys and the command line
#---------------------------------------------------------------------------------------

############################################
# Task 1 - Import sys and use python with the command line.

import sys

class Animal():
    def eat(self):
        print('yum')
class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Robot():
    def move(self):
        print('... move move move..')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')

class SuperRobot():
    def __init__(self):
        #This class contains 3 objects
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot method
    
machineDog = SuperRobot()
machineDog.move()
machineDog.bark()

name = sys.argv[1]
age = sys.argv[2]

print(name)
print(age)