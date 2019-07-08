# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:49:19 2019

@author: Hengky Sanjaya
"""

#interpolation
import numpy as np
import math

p = np.array([44 * math.pi / 180, 46 * math.pi / 180])
q = []
for i in p:
    q.append(math.tan(i))
    

p1 = 45 * math.pi/ 180

def newton_interpolation(p, q, p1):
    b0 = q[0]
    b1 = (q[1] - q[0]) / (p[1] - p[0])
    
    return b0 + b1 * (p1 - p[0])


print(newton_interpolation(p, q, p1))


def lagrange_interpolation(x_array, y_array, p1):
    n = len(x_array)
    
    total = 0
    for i in range(0, n):
        subtotal = 1
        for j in range(0, n):
            if(i != j):
                subtotal *= (p1 - x_array[j]) / (x_array[i] - x_array[j])
        total += subtotal * y_array[i]
    return total


print(lagrange_interpolation(p, q, p1))