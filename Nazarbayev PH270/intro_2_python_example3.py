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

p = input("Enter password: ")
password = "python"

while p != password:
    p = input("Password is wrong, try again: ")
    
print("\n Password: Correct ")
print("\n Here is the top secret information.")

# This will ask again and again until is correct.


