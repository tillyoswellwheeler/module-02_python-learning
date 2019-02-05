# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:53:28 2018

@tillyoswellwheeler: 612383362
"""
import learnpython_tilly_library

#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print("You have %d cheese!" % cheese_count)
#    print("You have %d boxes of crackers!" % boxes_of_crackers)
#    print("Man that's enough for a party!")
#    print("Get a blanket.\n")

# Uses the args to input parameters for the script to run
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Uses Global Variables and then calls the function and it's args
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Decides the parameters and does math on them
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Uses the global variables to call the args parameters, and does math on them
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

######
##Creating a new function and calls it 10 different ways #

#def coders_and_coffee(coders_count1, amount_of_coffee1):
#    print("You have %d coders!" % coders_count)
#    print("You have %d amount of coffee!" % amount_of_coffee)
#    print("Man that's enough for a app-solutely amazing time!")
#    print("Get some sleep.\n")
#    
#    return (coders_count1, amount_of_coffee1)

# 1. Give the function parameters directly into the args
print("Give function numbers directly.")
coders_and_coffee(29, 300)

# 2. Use Math with args
print("Give the function direct parameters and then add to them: ")
coders_and_coffee(29 + 1, 300 + 20)


# 3. Use global variables
print("Using global variables to give the args a value: ")

coders_count = 29
amount_of_coffee = 200

coders_and_coffee(coders_count, amount_of_coffee)

# 4. Use global variables and math
print("Using global variables to give the args a value then using math to change: ")

coders_and_coffee(coders_count + 20, amount_of_coffee * 2)

# 5. Use function to assign a value to new local varables
print("Using global variables and assigning new local variable values: ")

coders_count1, amount_of_coffee1 = coders_and_coffee(coders_count + 20, amount_of_coffee * 2)

# 6. Assign the local variables and print them
print("Prnting the newly assigned local variables and the private variables: ")

coders_count1, amount_of_coffee1 = coders_and_coffee(coders_count + 20, amount_of_coffee * 2)
print(coders_count1, amount_of_coffee1)

# 7. Call the local variables and add to them locally
print(coders_count1 + 30, amount_of_coffee1 + 100)

# 8. Create another function, call it and multiply together
coders_count1 = 29
amount_of_coffee1 = 200

#def print_twice_string_version(needs_printing):
#    to_return = str(needs_printing) * 2
#    
#    return to_return

print_twice_string_version(coders_and_coffee(coders_count1, amount_of_coffee1))

# 9. Same as above but looking at what saving as an int does

#def print_twice(array_input_twice):
#    to_return = array_input_twice[] * 2
#    
#    return to_return
#
#print_twice(coders_and_coffee(coders_count1, amount_of_coffee1)) 

# 10. Using global variables to give the args a value then using subtraction

print("Using global variables to give the args a value then using subtraction to change: ")

coders_and_coffee(coders_count1 - 20, amount_of_coffee1 - 2)

print_twice_string_version(coders_and_coffee(12 , 40))