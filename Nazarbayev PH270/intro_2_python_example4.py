# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:01:42 2020

@author: Julio
"""

''' Using numpy.zeros '''

from numpy import zeros

student_numb  = int(input("Enter number of students: "))

gpa = zeros(student_numb,float)

i   = 0

while i < student_numb:
    
    gpa[i] = float(input("Enter the GPA of student: "))
    i = i + 1
    
average = sum(gpa)/len(gpa)

print("Average GPA of class is: \n", average)