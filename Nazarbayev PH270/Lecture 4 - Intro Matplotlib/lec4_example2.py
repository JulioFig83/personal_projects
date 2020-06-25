# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:31:02 2020

@author: Julio
"""
'''Changing the y-scale of a plot'''

import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,20.1,0.1)
y = (10**x)*np.cos(x)**2

plt.plot(x,y)
plt.yscale("log")
plt.xscale("log")
plt.savefig("plots/chaning_scales_of_axis.pdf")

plt.show()

