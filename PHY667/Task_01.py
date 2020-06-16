# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:02:52 2020

@author: Julio
"""

'''Task 1 - Scientific Computing'''

# We want to use Python to calculate a physical
# quantity: Bohr Radius

import numpy as np

# setting up parameters

epsilon_0 = 8.85e-12
hbar      = 6.63e-34 / (2*np.pi)
mass_e    = 9.11e-31
charge_e  = 1.6e-19

# Bohr radius

a_0 = 4*np.pi * epsilon_0 * hbar**2 / (mass_e * charge_e**2)

# Printing the result out in a formated way v
# example %8.3e    8: 8 digits
#                  3: 3 decimal numbers
#                  e: scientific 

print('Bohr radius is %8.3e' %a_0)
