# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:07:29 2020

@author: Julio
"""

'''Third example, login information'''

# We want to create a program and put information 
# inside the program that a USER want to retrieve

# the USER needs a password
# If password is incorrect, deny 'entry' and ask again

p           = input("Enter password: ")
password    = "python"
max_trial   = 3

trial       = 1

while p != password:
    p = input("Password is wrong, try again: ")
    trial = trial +1
    
    if trial == max_trial:
        break 

if trial == max_trial:
    print("\n You exceeded the max. number of trials.")
    print("\n Please contact Support Team.")

else:   
    print("\n Password: Correct ")
    print("\n Here is the top secret information.")

# This will ask again and again until is correct.


