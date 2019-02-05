# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:40:27 2019

@tillyoswellwheeler: 612383362
"""

#---------------------------------
## BT Coding Interview Questions 
#---------------------------------
import string

#---------------------------------
## Task One -- Using for loops 
#---------------------------------

# Aim: Write the letters 'A' to 'Z'(in uppercase) to the console, placing each
#      letter on a newline.

alphabet = string.ascii_uppercase

def vertical_list(alphabet):
    for char in alphabet:
        print(char + '\n')

vertical_list(alphabet)

#---------------------------------
## Task Two --  
#---------------------------------

# Aim: For every third letter, write it to the console in lowercase instead.

alphabet_list = list(string.ascii_uppercase)

def every_third_letter(alphabet_list):
    for i in range(::3):
        

alphabet
#---------------------------------
## Task Three --  
#---------------------------------

# Aim: For every fourth letter, write its numeric position in the alphabet
#      to the console instead (eg// instead of outputting 'D' output '4').

#---------------------------------
## Task Four --  
#---------------------------------

# Aim: If a letter satisfies both rule 2 and rule 3, write out its numeric  
#      position followed by the letter in lowercase (eg//'L' is '12l')


