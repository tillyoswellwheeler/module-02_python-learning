# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:29 2018

@tillyoswellwheeler: 612383362
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheese!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def coders_and_coffee(coders_count1, amount_of_coffee1):
    print("You have %d coders!" % coders_count)
    print("You have %d amount of coffee!" % amount_of_coffee)
    print("Man that's enough for a app-solutely amazing time!")
    print("Get some sleep.\n")
    
    return (coders_count1, amount_of_coffee1)

def print_twice_string_version(needs_printing):
    to_return = str(needs_printing) * 2
    
    return to_return