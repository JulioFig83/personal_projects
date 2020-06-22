# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:01:42 2020

@author: Julio
"""

''' Using lists '''

student_numb    = int(input("Enter number of students: "))

gpa = [] # Empty list
i   = 0

while i < student_numb:
    
    av = float(input("Enter the GPA of student: "))
    gpa.append(av)
    
    i = i + 1
    
average = sum(gpa)/len(gpa)

print("Average GPA of class is: \n", average)