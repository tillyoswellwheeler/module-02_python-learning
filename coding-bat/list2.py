# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:24:46 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------
## Coding Bat -- List 2
#---------------------------------

#---------------------------------
## Counting Evens 
#---------------------------------

# End Goal = count_evens([2, 1, 2, 3, 4]) → 3
#            count_evens([2, 2, 0]) → 3
#            count_evens([1, 3, 5]) → 0

def count_evens(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
#            print("count= ", counter)    # for testing
    return (counter)

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5]) 

#print('final count= ', count_evens([2, 1, 2, 3, 4]))
#print('final count= ', count_evens([2, 2, 0]))
#print('final count= ', count_evens([1, 3, 5])) 

#---------------------------------
##  Has22
#---------------------------------

def has22(nums):
 for i in range(len(nums)-1):
  if nums[i] == 2:
     if nums[i+1] == 2:
      return True
 return False