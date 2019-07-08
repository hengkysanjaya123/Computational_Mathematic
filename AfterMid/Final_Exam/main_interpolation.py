# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:01:17 2019

@author: Hengky Sanjaya
"""
import numpy as np
import math

#1 Interpolation

p = np.array([44 * math.pi/180 , 46 * math.pi/180])
q = np.ones(len(p))

for i in range(len(p)):
    q[i] = math.tan(p[i])

def newton_interpolation2(p,q,p1):
    b0 = q[0]
    b1 = (q[1] - q[0])/(p[1] - p[0])

    order_1 = b0
    order_2 = b0 + b1 * (p1-p[0])

    return order_2

print(newton_interpolation2(p, q, 45*math.pi/180))

def newton_interpolation(p, q, p1):
    b0 = q[0]
    b1 = (q[1] -  q[0]) / (p[1] - p[0])
    
    return b0 + b1 * (p1 - p[0])

newton = newton_interpolation(p, q, 45 * math.pi/180)
print(newton)



# lagrange
def lagrange_interpolation(x_array,y_array,p1, n):
    total = 0
    for i in range(0,n):
        subtotal = 1
        for j in range(0, n):
            if(i != j):
                subtotal *= (p1- x_array[j]) / (x_array[i] - x_array[j])
        total += subtotal * y_array[i]
        
    return total

lagrange = lagrange_interpolation(p, q, 45 * math.pi/180, len(p))
print(lagrange)

exact = 1

print("Newton comparison : ", (abs(exact - newton) / exact) * 100)
print("Lagrange comparison : ", (abs(exact - newton) / exact)*100)