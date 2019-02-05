# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:18:40 2019

@author: tilly.oswellwheeler
"""
#---------------------------------
## CHAPTER 14 -- Databases
#---------------------------------

import sqlite3 # This is a very easy database engine. It is self-contained,
               # serverless, zero-configuration and transactional. 
import time
import datetime
import random

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


