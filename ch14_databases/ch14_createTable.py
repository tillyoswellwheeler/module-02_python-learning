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

conn = sqlite3.connect('task1.db') # Creates a database in RAM 
c = conn.cursor() # This code is a database object used by programs to 
                  # munipulate data in a set row by row. It points to data.
                  
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
# The CREATETABLE... command is SQL language and we can use SGL language
# when we call a c.execute function. SQL functions do note have to be in CAPS
# but it is useful to distinguish them from the programming language you use.
    
# Syntax for the table--'stuffToBuild' is the table name. 'unix', 'datestamp' 
# are column names. 'REAL' and 'TEXT' are the datatypes and format each column, 
# these are SQL language and that's why they are in CAPS.
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(14223222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close() # This closes the cursor object
    conn.close() # This closes the database object
    
create_table()
data_entry()

