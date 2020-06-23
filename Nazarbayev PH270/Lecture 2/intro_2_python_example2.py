
"""
Created on Sat Jun 20 16:59:11 2020

@author: Julio
"""

t = float(input("Enter temperature: "))

if t >= 100:
    print("Water is in gas state")
    
elif t >= 0 and t < 100:
    print("Water is in liquid state")
    
else:
    print("Water is in solid state")
    