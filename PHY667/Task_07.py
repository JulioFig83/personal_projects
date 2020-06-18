# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:16:38 2020

@author: Julio
"""

''' We are creating a 3D function '''

import numpy as np
import matplotlib.pyplot as plt

''' Creating a 2D function: sinusoidal 2D '''
# Like solutions of wave or Schr. equations.
# Rectangular boundary conditions

def fsin(x, y, m, n):
    z = np.sin( m*np.pi*x)*np.sin(n*np.pi*y)
    
    return z

# Defining the domain of x and y

x_domain = np.arange( -1, 1.01, 0.01 )
y_domain = np.arange( -1, 1.01, 0.01 )

# Using the command "len" will give is the size of an array

# Number of data points

nx = len(x_domain)
ny = len(y_domain)

# Using an empty 2D array to store the 'results'

z_range = np.zeros((nx,ny))

# defining parameters

m = 1.55
n = 0.55

for i in range(0,nx):
    
    for j in range(0,ny):
        
        z_range[i,j] = fsin(x_domain[i], y_domain[j], m, n ) 

''' Plotting it in 2D '''

plt.imshow( z_range, cmap=plt.cm.jet, interpolation='nearest' )
plt.show()





