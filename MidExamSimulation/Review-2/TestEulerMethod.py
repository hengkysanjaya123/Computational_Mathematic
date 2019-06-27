# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:08:59 2019

@author: Hengky Sanjaya
"""

#euler method
import math

h = 0.1
n = 10

y0 = 1
t0 = 0

for i in range(n):
    plt.plot(t0, y0 , 'o')
    m = math.pow(math.e, -1 * t0) + math.sin(y0)
    
    y1 = y0 + m * h
    
    t1 = t0 + h
    
    t0 = t1
    y0 = y1
    
    