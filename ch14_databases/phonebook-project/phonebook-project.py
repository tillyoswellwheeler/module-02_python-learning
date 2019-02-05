# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:18:40 2019

@author: tilly.oswellwheeler
"""
#---------------------------------
## CHAPTER 14 -- Phonebook project
#---------------------------------
import sqlite3 # This is a very easy database engine. It is self-contained,
               # serverless, zero-configuration and transactional. 
import time
import datetime
import random

#---------------------------------
## MVP--Residential Pseudo Code
#---------------------------------

# 1) Ask User input for 'surname' 
#        if surname is in database
#           go to user input location function. 
#        else tell the user they need a valid input.

def ask_surname():
    surname = input("What's the surname of the person you are looking for?")
    if surname == (SELECT * FROM Residential WHERE surname = %s, (surname, ):
        for row in c.fetchall():
            print (row)
    else:
        print("Error name not in phonebook")

ask_surname()

# 2) The user inputs the  their location:
#        if input is a valid string
#           search for 'surname' AND 'location' in residential table.

# 3) The user is presented with the relevant GROUP BY 'surname' AND 'location' 
#    which is ORDER BY a-z of first name of the surnames.
#
# 4) Ask the user if they want to sort the returned results by distance from
#    location:
#       if yes:
#           then order the returned group by results by the distance to location.
#       else:
#           return the a-z sorted results

#---------------------------------
## MVP--Business Pseudo Code
#---------------------------------

# 1) Ask User input for 'type' or 'name':
#       if input is type then return business type data
#       elif input is name then return the ask business name data
#       else return error and reask them the question
#
# 1.1) Ask User input if they want to sort by loaction rather than a-z 
#        if input is a valid string
#           render data sorted by location. 
#        else tell the user they need a valid input.


#---------------------------------
## Residential Pseudo Code
#---------------------------------

# 1) Ask User input for 'surname' 
#        if input is a valid string
#           go to user input location function. 
#        else tell the user they need a valid input.

# 2) The user inputs the  their location:
#        if input is a valid string
#           search for 'surname' AND 'location' in residential table.

# 3) The user is presented with the relevant GROUP BY 'surname' AND 'location' 
#    which is ORDER BY a-z of first name of the surnames.
#
# 4) Ask the user if they want to sort the returned results by distance from
#    location:
#       if yes:
#           then order the returned group by results by the distance to location.
#       else:
#           return the a-z sorted results

#---------------------------------
## Business Pseudo Code
#---------------------------------

# 1) Ask User input for 'type' or 'name':
#       if input is type then return the ask business type function
#       elif input is name then return the ask business name function
#       else return error and reask them the question
#
# 1.1) Ask User input for 'business type' 
#        if input is a valid string
#           go to user input location function. 
#        else tell the user they need a valid input.

# 1.2) Ask User input for 'business name' 
#        if input is a valid string
#           go to user input location function. 
#        else tell the user they need a valid input.

# 2) The user inputs the  their location:
#        if input is a valid string
#           search for 'surname' AND 'location' in residential table.

# 4) The user is presented with the relevant GROUP BY 'surname' AND 'location' 
#    which is ORDER BY a-z of first name of the surnames.
#
# 5) Ask the user if they want to sort the returned results by distance from
#    location:
#       if yes:
#           then order the returned group by results by the distance to location.
#       else:
#           return the a-z sorted results


conn = sqlite3.connect('task2.db') # Creates a database in RAM 
c = conn.cursor() # This code is a database object used by programs to 
                  # munipulate data in a set row by row. It points to data.
                  
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dynamicToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def dynamic_data_entry():
    unix = time.time() # Here we are using the imported time module
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')) # This uses the datatime module. The strf is format the string using %.
    keyword = 'Python'
    value = random.randrange(0, 10) # Using random imported module
    
    c.execute('INSERT INTO dynamicToBuild(unix, datestamp, keyword,value) VALUES(?, ?, ?, ?)', (unix, datestamp, keyword, value))
    conn.commit()

# This function is used to SELECT (all *) data FROM (selected table) to filter.
# You can use WHERE to further filter data inside each column.
def read_from_db_all():
    c.execute('SELECT*FROM dynamicToBuild WHERE value=8')
    for row in c.fetchall(): # Fetch all is liek the pull function in git.
        print(row)

#def
# Create the table first
 # Calling all the functions
def call_all_functions():
    create_table()
    dynamic_data_entry()
    read_from_db_all()

call_all_functions()
    
# Now we create a for loop to add random data to the database dynamically.
for i in range(10):
    dynamic_data_entry()
    time.sleep(1) # This is just because we are doing dummy data not needed in normal databases.
    
#----------  For more complicated databases you can use GROUP BY or ORDER BY 

    
c.close()
conn.close()


