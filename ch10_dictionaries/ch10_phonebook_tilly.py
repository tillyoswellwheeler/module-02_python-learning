 # -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:59:27 2018

@tillyoswellwheeler: 612383362
"""

#---------------------------------------------------------------------------------------
# CHAPTER TEN - Phonebook dictionary app/task
#---------------------------------------------------------------------------------------

############################################
# Practice with dict with function, subfunction, variable, user inputs and if/else

# Challenge 1: Sort by Name, Town/City and Lucky No
 
# Define the dictionary
# phoneBook_dict = {
#      'Rachel': [234, 4, 'SW125FD', 'london'],
#      'Martina':[938, 7, 'E35CH', 'london'],
#      'Sarika':[928, 2, 'CT36HH', 'Canterbury'],
#      'Harriet':[938, 9, 'W37DS', 'Woking']
#      }
 
 ## Assign the key to a variable
 
# namesList = list(phoneBook_dict.keys())
 
# ## Sort Name using the key sort function, very simple
# 
#names_sorted = sorted(phoneBook_dict.keys())
#print(names_sorted)
# 
# ## Sort Town/City alphabetically using the lambda key value function [3]
# 
#towns_sorted = sorted(namesList, key=lambda k:phoneBook_dict[k][3])
 
## Sort Town/City alphabetically using the lambda key value function [1]
 
#sorted(namesList, key=lambda kv:kv[1])
 
 ## Use user input to assign new values to 

#phoneBook_dict ['Tilly'] = [234, 2, 'CT34HH', 'Herne Bay']

#phoneBook_dict.update({'Tom':[298, 8, 'SW187dh', 'London']})

#print(phoneBook_dict)

###########################################################
# Using functions and subfunctions to make dry-er code

#---------------------------------------------------------
#    Putting all global variables into local ones
#---------------------------------------------------------

def the_phonebook():
    phonebook_dict = { }
    namesList = list(phonebook_dict.keys())

    return phonebook_dict_list(namesList)

def user_contacts_input():
    update_requested = input("Update your phonebook with a new contact?\n")
    if update_requested == "yes":
        the_phonebook()
    else:



def sort_name(phonebook_dict_list(namesList)):
    names_sorted = sorted(phonebook_dict.keys())
    print(names_sorted) 
    return

def sort_town_city(phonebook_dict_list(namesList)):
    towns_sorted = sorted(namesList, key=lambda k:phonebook_dict[k][3])
    print(towns_sorted)
    return

def sort_lucky_number(phonebook_dict_list(namesList)):
    lucky_number_sorted = sorted(namesList, key=lambda k:phonebook_dict[k][1])
    print(lucky_number_sorted)
    return

def add_to_phonebook_dict():
    name = input("The name of the contact you want to add? " )
    phone_number = input("What's your contacts last three digits? ")
    lucky_number = input("What's your contacts lucky number? ") 
    postcode = input("What's your contacts postcode? ")
    town_city = input("What's your contacts twon or city? ")
    phonebook_dict.update({name:[phone_number, lucky_number, postcode, town_city, age]})
    
    return phonebook_dict()
    
def queens_age(phonebook_dict):
    queenAge = 92
    age = int(input("What's your contacts age? "))
    phonebook_dict.update({name:[phone_number, lucky_number, postcode, town_city, queenAge - age]})    
    
    return phonebook_dict

def add_and_sort(phonebook_dict):
    add_to_phonebook_dict()
    sort_name(phonebook_dict)
    sort_town_city(phonebook_dict)
    sort_lucky_number(phonebook_dict)
    queens_age(phonebook_dict)
    
add_and_sort(phonebook_dict)

print(phonebook_dict)
print(queens_age)

 
 # Challenge 2: Add two more items in the value list and sort by years different to Queen's age and wtite file to dict file.

f = open("phonebook.txt", "r+")
f.write(str(sorted(phonebook_dict.items())))
f.close()
 