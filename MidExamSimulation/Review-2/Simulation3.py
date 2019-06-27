# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:05:50 2019

@author: Hengky Sanjaya
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import *

data = np.array([
            12.5, 11.4, 15.7,13.1,12.9, 14.1
        ])

mean = np.mean(data)
std = np.std(data, ddof=1)

Q = np.percentile(data, [25, 50, 75])

print("mean", mean)
print("standard deviation ", std)
print("Q1, Q2, Q3 " , Q)

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(1, 1, 1)

plt.errorbar(1, mean , std, capsize=5, color='b')
plt.plot(1, mean, 'sk')

plt.boxplot(data, positions=[2])

ax.set_xlim([0,3])
ax.set_ylim([10, 17])
plt.xticks([1, 2], ["Error bar", "Boxplot"])
ax.set_title("Figure 1")

plt.show()
print("\n2-----------------------------------------------")

def mycos(x,n):
    total = 0
    for i in range(n):
        total = total + (-1)**i * (4*x)**(2*i) / math.factorial(2*i)
    return total
    

x = 3/8 * 3.14
n = 20

value = mycos(x, n)
actual = np.cos(4*x)
print("mycos", value)
print("actual", actual)


print("\n3-----------------------------------------------")

A = np.array([
            [3, 1, 0,0],
            [2, 3, 2, 0],
            [1, 2, 4, 1],
            [0, 1, 1,2]
        ])
b = np.array([
            [1],
            [1],
            [1],
            [1]
        ])
    
x = np.linalg.solve(A, b)
print(x)

det_A = np.linalg.det(A)
print("Determinant A", det_A)

norm_b = np.linalg.norm(b)
print("norm b ", norm_b)


print("\n5-----------------------------------------------")

def trapezoid(f, a, b, n):
    h = (b-a)/n
    s = (f(a) + f(b)) / 2
    for i in range(1,n):
        s = s + f(a + i * h)
    return h * s

def gauss(f, a, b, n):
    zeta = np.array([0.774597,0, -0.774597])
    w = np.array([0.555556,0.888889,0.555556])
    x = (b+a)/2 + (b-a)/2 * zeta
    area = (b-a)/2 * np.sum(w * f(x))
    return area

f = lambda x: 2 + np.sin(x)
a = 0
b = np.pi / 2
n = 2
print(trapezoid(f, a, b, n))
print(gauss(f, a, b, n))

exact = quad(f, a, b)[0]
print("Exact ", exact)



