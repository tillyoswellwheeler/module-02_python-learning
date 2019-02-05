# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:38:32 2018

@tillyoswellwheeler: 612383362
"""

#Check user state, they are registered or unregistered
class User(object):
    def __init__(self, username, passcode):
        self.username = username
        self.passcode = passcode
    
    def ask_user_state(self, username, passcode):
        print("Are you a customer with us?")
        if print == "y":
            user_registered(username, passcode)
        if print == "n":
            user_unregistered(self)
        else:
            print("Invalid input")
    
    def user_registered(username, passcode):
        customer_account(username, passcode, credit)
        
class UnregisteredUser(object):
    def user_unregistered(self, username, passcode):
        print("Do you want to become a customer with us?")
        if print == "y":
            user_register_process(self, username, passcode)
        if print == "n":
            print("That's fine")
            ask_user_state(self, username, passcode)
        else:
            print("Invalid input")
            
#      Filler function for now      
    def user_register_process(self, username, passcode): 
        print("register now")
            
class RegisteredCustomer(User):
    def __init__(self, username, passcode, credit):
        self.username = username
        self.passcode = passcode
        self.credit = credit
    
    def customer_account(username, passcode, credit):
        check_username(username)
        check_passcode(passcode)
        check_balance(credit)
        
    def check_username(username, system_username):
#        Import database data
        username = input("What's your username?")
        if username == system_username:
            check_passcode(passcode, system_passcode)
        if username != system_username:
            print("Invalid username")
        else:
            print("Not a valid imput")
            
    def check_passcode(passcode, system_passcode):
        #        Import database data
        passcode = input("What's your passcode?")
        if passcode == system_passcode:
            transaction_type(balance, purchase)
        if passcode != system_passcode:
            print("Invalid passcode")
        else:
            print("Not a valid imput")
#User enters username




#Users username is checked against the system

#User enters passcode

#Users passcode is checked against the system

#User selects a transaction type from a numbered list

#User is sent back to the start
