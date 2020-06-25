# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:52:10 2020

@author: Julio
"""

''' Introduction to Matplotlib '''

import matplotlib.pyplot as plt
import numpy as np 


x  = np.arange(0,20.1,0.1)
y  = np.cos(x)
y1 = np.exp(-x/5)*np.cos(x) # Damped oscillator

plt.plot(x,y, label="Oscillation 1", color = 'g', linestyle="--")
plt.plot(x,y1, label= "Damped oscillation", color = 'b')
plt.xlabel("$x$-axis", size = 12)
plt.ylabel("$cos(x)$", size=14)

# The way to save plots is like:
# it is done before 'showing it'.
plt.legend()
plt.savefig("plots/damped_oscil_plot_w_label_axis_and_latex.pdf")

plt.show()






