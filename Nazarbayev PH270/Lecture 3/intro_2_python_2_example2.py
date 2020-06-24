# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:38:38 2020

@author: Julio
"""

'''We want to calculate the factorial of a number'''

''' Defining a function '''

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

f_5   = factorial(5)
f_123 = factorial(123)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import cos, sin

def polar2cart(r,theta):
    x = r*cos(theta)
    y = r*sin(theta)
    
    return x,y

r_0     = 10
theta_0 = 0.3

x_0,y_0 = polar2cart(r_0,theta_0)

print(x_0,y_0)
    

    
    
    
    
    
    
    
    