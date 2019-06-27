# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:52:46 2019

@author: Hengky Sanjaya
"""

# Newton's Method

f = lambda x : x**2
f_1 = lambda x : 2 * x
f_2 = lambda x : 2

x0 = -1.5
x1 = x0 - f_1(x0) / f_2(x0)

while(x1 != x0):
    x0 = x1
    x1 = x0 - f_1(x0) / f_2(x0)
    
print(x1)    
    