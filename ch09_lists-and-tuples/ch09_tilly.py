# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:50 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER NINE - lists and Tuples
#---------------------------------------------------------------------------------------

############################################
# Using lists

my_favourite_fruits = ['apple', 'orange', 'banana']

mixed_list = ['car', 'orange', 55, 'time', 'bummer']

mixed_list[0]

mixed_list[1]

mixed_list[2]

mixed_list[-1]

print(mixed_list[0])

print(mixed_list[1])

print(mixed_list[2])

print(mixed_list[-1])

mixed_list.remove(55)

mixed_list.append('again')

print(mixed_list[0])

print(mixed_list[1])

print(mixed_list[2])

print(mixed_list[-1])

y = mixed_list

print(y)

z= y + mixed_list

print(z)

#######################################
## Using Range with Lists

mixed_list[2:4]

print(mixed_list[2:4])


########################################
##### Sorting Lists

#sorted_mixed_list = sorted(mixed_list)

sorted_mixed_list = sorted(mixed_list, reverse=True)

print(sorted_mixed_list)

list_to_be_sorted = [1, 3, 7, 2, 44, 21]

#list_to_be_sorted.sort()

list_to_be_sorted.sort(reverse=True)

print(list_to_be_sorted)

#########################################
## Tuples

a = [0 ,1 ,2, 3, 4, 5 ,6 ,7 ,8 ,9]

#del a[-1]

b = (0 ,1 ,2, 3, 4, 5 ,6 ,7 ,8 ,9)

#del b[-1] You cannot do this tuples are immutable that means they are unchangeable

#a[3] = 50

#b[3] = 50 You cannot do this because the data type tuple is immutable

#a.append(2)

#b.append('z') You cannot append because this data type is immutable
print(a)
print(b)

#############################################
#Comparing lists and tuples

comparison_a_b = sorted(a, reverse=True)
if a == b:
    print(True)
else:
    print(False)
    
###############################################
### Lambda

#Variables to be used:    

my_favourite_fruits = ['apple', 'orange', 'banana']

mixed_list = ['car', 'orange',  'orange', 'time', 'bummer']

list_to_be_sorted = [1, 3, 7, 2, 44, 21]

b = (19 ,18 ,27, 36, 45, 54 ,63 ,72 ,81 ,90)

a = [29 ,18 ,27, 36, 45, 54 ,63 ,72 ,81 ,90]

c = [19 ,28 ,37, 36, 45, 54 ,63 ,72 ,81 ,90]

c1 = ['ad', 'ab', 'de', 'fe']

b1 = ('da', 'fe', 'th', 'wd', 'ab', 'de')

a1 = ('rf', 'gt', 'hy', 'ac')

a2 = ['ceo', 'cto', 'ctio']
b2 = ('ceo', 'cto', 'ctio')
c2 = ['abc', 'dba', 'tba']

#tuples_within_list = [('ab', 3, my_favourite_fruits), ('ba', 1, mixed_list), ('cc', 5, list_to_be_sorted)]

#sorted(tuples_within_list, key=lambda s:s[1])

#print(sorted(tuples_within_list, key=lambda s:s[1]))

#print(sorted(tuples_within_list, key=lambda s:s[2][1]))

#Accessing the elements within the list

#tuples_within_list = [('ab', 3, a1), ('ba', 1, b1), ('cc', 5, c1)]
tuples_within_list = [('ab', 3, a2), ('ba', 1, b2), ('cc', 5, c2)]


print(sorted(tuples_within_list, key=lambda s:s[2][1][1])) 