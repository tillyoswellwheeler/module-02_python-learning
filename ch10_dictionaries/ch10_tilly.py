# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:59:27 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER TEN - Dictionaries in Python
#---------------------------------------------------------------------------------------

############################################
# Creating an empty dictionary and then adding to it

salary = {}

salary['al'] = 2000

print(salary)

salary['tilly'] = 3000

print(salary)


salary['chen'] = 5000

###########################################
# Printing a value from a dictionary

print(salary['chen'])

# syntax is print(dictionary_name['key_name']) = Value_amount

############################################
# Adding to a value within a dictionary

salary['al'] += 200

print(salary)


############################################
#Creating a telephone book

tel = { 'bob': 323239, 'rob': 9382097, 'toby': 23984029}

print(tel)

class_tel = {'rachel': 819, 'Amaniat': 151, 'tilly': 369}

print(class_tel)

class_tel['Martina'] = 324

print(class_tel)

############################################
#Deleteling items in a dictionary

del class_tel['tilly']

print(class_tel)

############################################
## Methods for a dictionary

# .keys() & .values()

print(class_tel.keys())

print(class_tel.values())

class_tel_keys = list(class_tel.keys())

list(class_tel_keys)

print(class_tel_keys)

#######################################
## Searching in Dictionaries
### A non working version of the expression

dictionary_to_be_searched = {'rachel': 819, 'Amaniat': 151, 'tilly': 369}

k = "object_that_needs_searching"

if k in dictionary_to_be_searched:
    print(k, ':', dictionary_to_be_searched[k])
else:
    print(k, 'Not Found')
    
########################################
# Using the Lambda function to sort
    
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
print(labels)
    
############ Sorting in ascending
    
labels.sort(key=lambda v:counts[v])

sorted(labels, key=lambda k:counts[k])

###########################################
### Returning both key and value values
sorted(counts.items(), key=lambda kv: kv[1])

########### Sorting in descending

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())

#############################################
## Returning both keys and values for descending
sorted(densities.items(), key=lambda kv:kv[1], reverse=True)

##############################################
##  Sorting by the second values of the dictionary in descending order

 ### I need to check whether this just means sorting by the words second letter????
 
