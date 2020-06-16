# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:15:27 2020

@author: Julio
"""

# Task 02: Using the for loop 

'''Calculating the charge of a discharging
capacitor'''

import numpy as np

# Parameters

C   = 200e-6      # Capacitance 200 microfarrad
R   = 300e3       # Resistance in ohms
V_0 = 10          # Voltage

# Using for loop command to vary the time 

q_0 = C*V_0

for i in range(0,10):
    t   = 50*i
    q   = q_0*np.exp(-t/(R*C))
    
    print('q( %8.3f sec ) = %8.3e Coulomb = %8.3f microC' %(t,q, q/(1e-6)))
    