# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:09:09 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER FIVE - Object Orientated Programming
#---------------------------------------------------------------------------------------

############################################
# Task 1 - Creating out first class

#class Customer(object):
#    
#    """A customer of ABC Bank with a checking account. Customers have the following properties:
#    Attributes:
#        name: A string representing the customer's name
#        balance: A float tracking the current balance of the customer's account. """
#        
#    def _init_(self, name, balance=0.0):
#        #Return a Customer object whose name is *name* and starting balance is *balance*.
#        self.name = name
#        self.balance = balance
#    
#    def withdraw(self, amount):
#        # Return the balance remaining ater withdrawing *amount* dollars.
#        if amount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#            self.balance -= amount
#            return self.balance
#        
#    def deposit(self, amount):
#        # Return the balance remaining after depositing *amount* dollars.
#        self.balance += amount
#        return self.balance 
#        

############################################  
# Changing Task 1 to have an else if statement
#        
#class Customer(object):
#    
#    """A customer of ABC Bank with a checking account. Customers have the following properties:
#    Attributes:
#        name: A string representing the customer's name
#        balance: A float tracking the current balance of the customer's account. """
#        
#    def _init_(self, name, balance=0.0):
#        #Return a Customer object whose name is *name* and starting balance is *balance*.
#        self.name = name
#        self.balance = balance
#    
#    def withdraw(self, withdrawAmount):
#        # Return the balance remaining ater withdrawing *amount* dollars.
#        if withdrawAmount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#            
#        else:
#            self.balance -= withdrawAmount
#            
#        return self.balance
#        
#    def deposit(self, depositAmount):
#        # Return the balance remaining after depositing *amount* dollars.
#        self.balance += depositAmount
#        return self.balance  
#    
#customer1 = Customer('Jason Taylor', 'jason', 1000.0)

#############################################
# Task 2 & 3 -- Inheritance
#
#class Animal():
#    def eat(self):
#        print('yum')
#class Dog(Animal):
#    def bark(self):
#        print('Woof!')
#class Cat(Animal):
#    def meow(self):
#        print('Meow!')
#class Pug(Dog):
#    def waddles(self):
#        print('there it goes slowly')
#class Bordercollie(Dog):
#    def sprints(self):
#        print('Now you see him, now you.....')
#        
#Snoopy = Bordercollie()
#Snoopy.bark()
#Snoopy.eat()
#Snoopy.sprints()

###############################################
# Creating our own mini program using OOP

#class Employee():
#    def __init__(self, company, timeWorked=0):
#        self.company = company
#        self.timeWorked=timeWorked
#        
#    def company_name(self):
#        if self.company = '
#class BtEmployee():
#class BtFurtherCohort():


###############################################
# Task 4 -- Association

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

    

