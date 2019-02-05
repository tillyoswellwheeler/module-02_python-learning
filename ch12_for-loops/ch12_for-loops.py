# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:24:46 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------
## For Loops
#---------------------------------

##--------------------------------
# TASK 1
#---------------------------------

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print(item)
    
#  This example below shows that the variable X is a placeholder and not linked to the lists data.    
#for x in my_shopping_cart:
#    print(x)

##--------------------------------
# TASK 2
#---------------------------------

values = [875, 23, 451]

for val in values:
    print("--->"+str(val))


##--------------------------------
# TASK 3
#---------------------------------

values = ['this', 55, 'that']

for item in values:
    print("***", item)


##--------------------------------
# TASK 4
#---------------------------------

for char in "Yes":
    print(char)

##--------------------------------
# TASK 5
#---------------------------------

new_tuple = (32, 54, 87, 98)

for items in new_tuple:
    print(items)
    
##--------------------------------
# TASK 6
#---------------------------------

salaries = {'al':20000, 'bo':50000, 'ced':1500 }

# This prints the key without needing to turn into a list
for people in salaries:
    print(people)
    
# This prints the values
list_values_salaries=list(salaries.values())   

sorted(list_values_salaries) 
for pay in list_values_salaries:
    print(pay)

# This prints the key and values
#key_value = sorted(salaries.items(), key=lambda kv:kv[1][1])
#for people, pay in key_value:
#    print(people, pay)
# The above is not functioning
    
##--------------------------------
# TASK 7
#---------------------------------

densities = {'iron': 7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals = list(densities.keys())

metals.sort(reverse=True, key=lambda m:densities[m])

for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal, densities[metal]))
    
##--------------------------------
# TASK 8
#---------------------------------

#for metal in metals:
#    if (metal, densities[metal]) >= 8.0:
#        print('{0:>10} = {1:5.1f}'.format(metal, densities[metal]))
#    else:
#        print("Boom")
# The above is not working    

##--------------------------------
# TASK 9
#---------------------------------

def array_calculation():
    array_sum = [1, 1, 2, 4, 5, 7]
    total = 0
    for val in array_sum:
        total += val
    print('Total:', total)
    return

#---------------------------------
# TASK 10
#----------------------------------
        
colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']
d = {} # build an empty dictionary
for item in colours:
    if item not in d:
        d[item] = 0
        print(d, 'first mention')
    else:
        d[item] += 1
        print(d)
print('Completed Dictionary:',d)

#---------------------------------
# TASK 11
#---------------------------------
for i in range(2, 20):
    print(i)
    
#---------------------------------
# TASK 12
#---------------------------------

nums = [2, 3, 345, 654, 234, 23]
for n in nums:
    if n >100:
        print('found:', n)
        break
    
#---------------------------------
# TASK 13
#---------------------------------
outer_vals=[1,2,3]
inner_vals=['a','b','c'] 

for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
        
#---------------------------------
# TASK 14
#---------------------------------
        
for i in range(1,7):
    for j in range(1,11):
        print('{0:>3}'.format(i*j), end='')
    print('\n')