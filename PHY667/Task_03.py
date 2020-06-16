# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:29:54 2020

@author: Julio
"""

# Task 03: Random number generator and IF statement

'''Coin tossing game [Heads/Tails]'''

from numpy.random import rand

# Specifying condition for Head and Tail
# Head:     r > 0.5
# Tails:    r <= 0.5

# We want to count number of head and tail

# specifying counter variables (variables that count # of heads/tails)

h = 0
t = 0



for i in range(0,1000):
    
    r = rand()
    
    if r > 0.5:
        h = h +1
    else:
        t = t +1
    
print('We get %3d heads and %3d tails'%(h,t))

