# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:59:00 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER TEN - Dice Game
#---------------------------------------------------------------------------------------

# The dice game take the sum of two di and calculates whether it is odd or even

#Pseudo code

# Import randint
from random import randint

# A function is defined with no arguments

def dice_game():
    odd_even_result = odd_or_even(result)
    odd_even_result = str(odd_even_result)
    to_play = input("Do you want to play a game? ")
    if to_play == 'y':
        user_result = input("Which do you guess odd or even or quit the game? ")
        if user_result == 'even':
            
            
            
            
            print("Number even, you win")
        else:
            print("Number odd, you lose! ")
    else:
        print("Too bad, you odd ball")
    
        
# Two values created by the randint function
def dices_random_number():
    dice1 = randint(0, 6)
    dice2 = randint(0, 6)
    
    print(dice1, dice2) #Testing that the subfunction is working
    
    return (dice1, dice2)

# The two randint numbers are added together
def dice_added_together():
    dice1, dice2 = dices_random_number()
    dice_sum = dice1 + dice2
    
    return (dice_sum)

# There is a function that works out if the sum of dice is odd or even
def odd_or_even(result):
    if result % 2 == 0:
        even = result 
        return (even)
    
    else:
        odd = result
        print("Number odd")
        return (odd)


dice_game()
# Tell user if they were right or wrong
# Game continues until user 'quits'