#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:09:51 2019

@author: matildaoswell-wheeler
"""
#---------------------------------
## CHAPTER 13 -- OOP Revision 
#---------------------------------

##--------------------------------
# TASK 1 -- Create a Person Class
#---------------------------------

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print("Gender not recognised!")
    
# Adding more generic functions
    def greetingInformal(self):
        print("Hi", self.name)
    def greetingFormal(self):
        if self.isMale:
            print("Welcome, Mr ", self.name)
        else:
            print("Welcome, Madame ", self.name)
# Adding filters to the class
    def greetingAgeBased(self):
        if self.age < 18:
            print("Welcome, young ", self.name)
        elif self.age > 60:
            print("Welcome, venerable ", self.name)
        else:
            self.greetingFormal()

# Creating a subclass for the Person class
class Wizard(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm')
    def greetingFormal(self):
        print("Welcome, Mr ", self.name, end=" ")
        print("- you're a fine Wizard!")
    def spell(self):
        print("Expelliarmus!")
            
## This is an instance object of the class above

p1 = Person('Tilly', 26, 'f')
p2 = Person("Dave", 26, 'm')
print(p1.name)
print(p1.greetingInformal())
print(p2.greetingFormal()) # Why does printing return the value? Is it the auto return function in Python?
p2.greetingFormal()

# Testing the filter function for greetingAgeBased(self)
p3 = Person("Middle", 40, 'm')
p4 = Person('Young', 17, 'f')
p5 = Person("Old", 61, 'm')
p3.greetingAgeBased()
p4.greetingAgeBased()
p5.greetingAgeBased()

# Testing the Wizard subclass functions
p6 = Wizard('Tilly', 26, 'f')
p7 = Wizard("Dave", 26, 'm')
p6.greetingFormal()
p7.greetingFormal()
p7.spell()


