# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:24:46 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER TEN - While Loops
#---------------------------------------------------------------------------------------

##--------------------------------
# TASK 1
#---------------------------------

x = 33
while x >= 1:
    print(x, ': ', end='')
    x = x / 2
print(x)

##--------------------------------
# TASK 2
#---------------------------------

#Breaking down the problem
# The tiangular numbers are a simple addition of a row to an equilateral triangle
#sum of all rows added equals the triangular number. EG// nth = 4 : 1+2+3+4 or nth=5:1+2+3+4+5

## Step 1 -- You must give a variabe space for the triangular sum to go to

## Step 2 -- You then want to write while n = 1 minus 1. This is because the sum above rewritten 
#looks like: n=4: (4-3) + (4-2) + (4-1) + 4

#You want to give n and then (n-1) + n


def triangular_numbers(n):
    triangular_sum = 0
    while n >= 1:
        triangular_sum = triangular_sum + n
        n = n-1
    print(triangular_sum)

triangular_numbers(4)

##--------------------------------
# TASK 3
#---------------------------------

# Student marks and while loops for checking through marks, make sure to define m to 0

def student_marks():
    mark = 1
    while mark > 0:
        mark = input("Enter your mark: ")
        mark = int(mark)
        print("Mark is", mark, end='')
        if mark >= 70:
            print("-- Well done, First Class")
        elif mark >= 40:
            print("-- Pass")
        else:
            print("-- That's a fail")

student_marks()

##--------------------------------
# TASK 4
#---------------------------------

# Creating a break statement

i = 55
while i > 10:
    print(i)
    
    i = i * 0.8
    if i==35.2:
        break

##--------------------------------
# TASK 5
#---------------------------------

# Creating a print name function whilst the user selects yes


#### Attempts to separate out the functions
#def ask_user_name():
#       name = input("What's your name? ")
#       print("Hello {}".format(name)) 
#       return name
#
#def user_greeting(name):
#    name = input("Do you want to say hi again? ")
#    while input == 'y':
#        ask_user_name()
#    print("We are done")
#      
#user_greeting(name)

# Chen's version

def user_greeting():
    while True:
        name = input("Enter name: ")
        if name == 'done':
            break
        print('Hello', name)

user_greeting()

#---------------------------------------------------------------------------------------
# CHAPTER TEN - Guessing Game
#---------------------------------------------------------------------------------------

from random import randint

# The imported function is below:
def guess(attempts, end_range):
    number = randint(1, end_range)
    print("Welcome! Can you guess my secret number?")
    # My code is below:
    # Tell the user how many attempts/guesses they have.
    
    print("You have {} attempts to guess right".format(attempts))
    
    # Read in their guess into the game
    
    while attempts > 0:
        guess = input("What's my secret number? ")
        guess = int(guess)
        attempts -= 1
    
    # Compare their guess to the number which has been generated from the randint imported function
        if guess == number:
            print("You're a telepathic genius!")
            return
    # Tell them if their guess is right or wrong
            print(guess, " was correct")
    # Note if they are right how do we *break* out of the while loop?
    # If the while loop is looping not just on guesses but on the correct guess?
            print("You had", attempts, "left!")
            break
    # If their guess is wrong, tell them whether they are too high or too low
        elif guess != number:
            if guess >= number:
                print("Your guess was too high")
            elif guess <= number:
                print("Your guess was too low")
            else:
                return number
    
    print("END-OF-GAME: Thanks for playing!")
    print("The secret number was", number)

guess(3, 20)    
