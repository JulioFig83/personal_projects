# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:04:15 2020

@author: Julio
"""

# Task 04: While command

# Simulation of particle decay
# Finding the halflife

    # Halflife: number of *time* steps where 
    # total number of 'mother' particles is halved
    
from numpy.random import rand

# Number of initial atoms
N_0 = 100000

# N: Current of particles
N  = N_0 

# Number of timesteps
timestep = 0


# While this statement is true

while N > N_0/2:
    
    # Simulating the number of particles that decay in 
    # 1 timestep
    
    decay_prob = 0.05
    decaycount = 0      # number of particles decayed
    
    
    for i in range(0,N):
        
        r = rand()
        
        if r > decay_prob:
            decaycount += 0
        else:
            decaycount += 1
    
    # Updating number of particles
    
    N += - decaycount
    
    timestep += 1
        
    print('At time step %3d the number of remaining particle is %3d' %(timestep,N))
    
print("Halflife is %3d timesteps" %(timestep))
