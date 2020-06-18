# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:36:59 2020

@author: Julio
"""

'''Statistics in python'''

import numpy as np
import matplotlib.pyplot as plt

# Creating my own data 1D array

# 1k data points
data_points = 10000
mydata      = np.random.rand(data_points)

# Getting the average and sigma (stadnard deviation)

print('Average +- S.D = %8.3f +- %8.3f' %(np.average(mydata), np.std(mydata)))

# Shows the distribution of mydata

plt.plot(mydata, 'b.')
plt.show()