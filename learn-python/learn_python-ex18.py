# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:18:31 2018

@tillyoswellwheeler: 612383362
"""

# this one takes the args within the function

def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
# This is a better more Object oriented way of expressing the above
    
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
        
#this take one argument

def print_one(arg1):
    print("arg1: %r" % arg1)
    
# this one takes no arguments
    
def print_none():
    print("I got nothin'.")

print_two("tom", "toby")
print_two_again("tom", "toby")
print_one("OO")
print_none()