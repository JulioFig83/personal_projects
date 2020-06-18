# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:37:47 2020

@author: Julio
"""

''' 2 Main sections: 
    
1. Apply math functions to import 
a p.d.f (like Maxwell distribution)
and calculate the pot. energy function 
from U = -kT ln P

2. Order-2 polynomial fitting the pot. function'''

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyval

# Obtaining the data
dataps = 100
X      = np.random.poisson(lam = 5, 
                         size = dataps)

# Obtaining the Frequency Distribution Histogram

P, bins = np.histogram(X, bins = 100)
xbin = 0.5*(bins[:-1] + bins[1:])

# Calculating the potential energy function

U = -np.log(X) # energy in units of kT

# PLotting the potential

plt.plot(xbin, U, 'b.')


# 2-order polynomial fitting 
# Least squares polynomial fit

p = np.polyfit(xbin, U, 2)
print("This plot is fitted to the equation")
print("%8.3fx^2 + %8.3fx + %8.3f = 0" %(p[0],p[1],p[2]))

''' Plotting such equation '''

# Calculating values of a polynomial with polyval

# Domain 
xfit = np.arange(1.5, 11.0, 0.01)

# Range
yfit = polyval(xfit, (p[2], p[1], p[0]))

plt.plot(xfit, yfit, 'r')



#