# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:18:32 2020

@author: Julio
"""

'''Building histogram, a probability distribution'''

import numpy as np
import matplotlib.pyplot as plt

data_points = 10000
mydata      = np.random.normal(loc = 0.0, scale = 1.0, size = data_points)

# Building the histogram

# Touple number because np.histogram returns two values

P, bins = np.histogram(mydata, bins = 12)

# Plotting the histogram

xbin = 0.5*(bins[:-1] + bins[1:])

plt.plot(xbin, P)
plt.plot(xbin, P, 'r.')


