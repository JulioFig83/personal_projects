# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:47:45 2020

@author: Julio
"""

'''Reading data from files'''

import numpy as np

# First I'm going to create my own .txt file

# List of students grades
random_grade = np.random.rand(100) * 100

# List of students
random_studt = np.arange(1,101,dtype = int)

random_data  = np.transpose(np.array([random_studt,random_grade]))

np.savetxt("my_data.txt",random_data)

# Now that I have the data, lets read it and 
# do stuff with it.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# But now is only the second column

f = np.loadtxt("my_data.txt")

mean = sum(f[:,1])/len(f[:,1]) 
mean_sq = sum(f[:,1]**2)/len(f[:,0])

print("The mean is: \n", mean)
print("The mean squared is: \n", mean_sq)

# Calculating the geometric mean of n quantities
# geo_mean = exp((1/n)*sum(log(x_i)))

geo_mean = np.exp((1/len(f[:,0])*sum(np.log(f[:,1]))))
print("Geometric mean is: \n", geo_mean)



