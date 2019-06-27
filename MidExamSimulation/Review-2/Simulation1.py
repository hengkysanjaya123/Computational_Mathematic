# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:37:10 2019

@author: Hengky Sanjaya
"""

import numpy as np
import math
from sympy import *

print("\n1-------------------------------------------------------")

data = np.array([
            5.5, 1.1, 6.5, 4.9, 6.4,
            7.0, 1.5, 5.7, 5.9, 5.4,
            6.1, 1.2, 7.3, 6.1, 4.4
        ])

mean = np.mean(data)
print(mean)
std = np.std(data, ddof=1)
print(std)
Q = np.percentile(data, [25, 50, 75])
print(Q)


#
print("\n2-------------------------------------------------------")
A = np.array([
            [6,2,0,0,0],
            [-1,7,2,0,0],
            [0,-2,8,2,0],
            [0,0,3,7,-2],
            [0,0,0,3,5]
        ])

b = np.array([
            [2],
            [-3],
            [4],
            [-3],
            [1]
        ])

x = np.linalg.solve(A, b)
print(x)

inverse_A = np.linalg.inv(A)
print(inverse_A)

det_A = np.linalg.det(A)
print(det_A)


print("\n3-------------------------------------------------------")

def ln1_x(x,n):
    total = 0
    for i in range(n):
        value = ((-x)**(i+1)) / (i+1)
        total += value
    return total

x = 0.5
ln1_8 = ln1_x(x, 8)
ln1_16 = ln1_x(x, 16)
print("ln1_8 " , ln1_8)
print("ln1_16 ", ln1_16)

actual_value = math.log(1-x)
print("Actual " , actual_value)


error_8 = actual_value - ln1_8
error_16 = actual_value - ln1_16
print("error 8 ", error_8)
print("error 16 ", error_16)

print("relative error 8 {}%".format(error_8 / actual_value * 100))
print("relative error 16 {}%".format(error_16/actual_value * 100))

print("\n4-------------------------------------------------------")

def trapezoid(f, a, b, n):
    h = (b-a) / float(n)
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s = s + f(a + i * h)
    return h * s

a = 0
b = 2
n = 4

f = lambda x: 2*x**4 + 6*x**3 - 2*x

trape = trapezoid(f, a, b, n)
print("Trapezoid ", trape)


x = symbols('x')
inte = integrate(f(x),x)
exact = abs(inte.subs(x,0) - inte.subs(x,2))
print("Exact " , float(exact))

error = (exact - trape) / exact * 100

print("Error ", error)







