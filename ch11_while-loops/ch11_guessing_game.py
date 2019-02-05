# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:02:28 2018

@tillyoswellwheeler: 612383362
"""

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
