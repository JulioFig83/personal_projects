# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:58:11 2020

@author: Julio
"""

import numpy as np
import matplotlib.pyplot as plt

'''Basic reading, plotting and writting files '''

# Reading txt file into an array

X = np.loadtxt("data.txt")

# Making simple plot of data

plt.plot(X[:,0], X[:,1])

# Writting a .csv file

np.savetxt('data.csv', X, delimiter=',' ,fmt = '%8.3f')


# Writting a txt file 

# We open the file and store it in a variable called f
f = open("data_new.txt", 'w')

for i in X:
    f.write('x = %8.3f, y = %8.3f \n' %(i[0], i[1]))
    
f.close()
