# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:57:59 2020

@author: Julio
"""

''' We are going to define and use a function
to be specific, a 1D Gaussian function.'''

import numpy as np
import matplotlib.pyplot as plt

# Creating the function

def fgauss( x, A, b ):
    y = A*np.exp( -b*x**2 )
    
    # A is the amplitude, b is coefficient, x is domain
    
    return y

# Defining the domain of the funciton

x_domain = np.arange(-5, 5.1, 0.1)

# Defining the range of the function with given parameters

y_range  = fgauss(x_domain, 1, 1)

''' Now with other parameters '''

y_range2 = fgauss(x_domain, 0.5, 0.5)

# Plotting (and customizing)

plt.plot(x_domain, y_range, 'k.')
plt.plot(x_domain, y_range2, 'b')
plt.show()



