# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:22:41 2019

@author: Hengky Sanjaya
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import *

plt.style.use('ggplot')

data = np.array([
            5.5, 1.1, 6.5, 4.9, 6.4,
            7.0, 1.5, 5.7, 5.9, 5.4,
            6.1, 1.2, 7.3, 6.1, 4.4
        ])


fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(1, 1, 1)

mean = np.mean(data)
std = np.std(data, ddof=1)
Q = np.percentile(data, [25, 50, 75])

for i in data:
    plt.plot(1, i, 'o', color='red')
    
plt.errorbar(2, mean, std, capsize=5, color='b')
plt.plot(2, mean, 'sk')

plt.boxplot(data, positions=[3])

up = mean + std
down = mean - std
ax.text(2.15, up , "x + s = " + str(round(up,2)))
ax.text(2.15, mean, "x = " + str(round(mean, 2)))
ax.text(2.15, down, "x - s = " + str(round(down, 2)))

ax.text(3.15, Q[0], "Q1 = " + str(Q[0]))
ax.text(3.15, Q[1], "Q2 = " + str(Q[1]))
ax.text(3.15, Q[2], "Q3 = " + str(Q[2]))

ax.set_xlim([0,4])
plt.xticks([1, 2, 3], ["Data", "Error Bar", "Boxplot"])


plt.show()

print("\n2--------------------------------------------------")

A =  np.array([
            [6, 2, 0,0,0],
            [-1, 7, 2, 0,0],
            [0, -2,8, 2, 0],
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
    
transpose_A = np.transpose(A)
print("transpose A \n", transpose_A)
transpose_b = np.transpose(b)
print("transpose b \n", transpose_b)

x = np.linalg.solve(A, b)
norm_x = np.linalg.norm(x)
print("norm vector x", norm_x)


print("\n3--------------------------------------------------")
def taylor_1(x, n):
    total = 0
    for i in range(n):
        total += math.pow(x, i)
    return total

x = 0.1
taylor1_5 = taylor_1(x, 5)
taylor1_10 = taylor_1(x, 10)
print("Taylor 5 term ", taylor1_5)
print("Taylor 10 term ", taylor1_10)

actual = 1 / (1 - x)
print("Actual " , actual)

print("Relative errors 5 terms", ((actual - taylor1_5) / actual) * 100)
print("Relative errors 10 terms", ((actual - taylor1_10) / actual) * 100)
    
    
print("\n4--------------------------------------------------")
    
def gauss(f, a, b):
    zeta = np.array([-0.577350, 0.577350])
    w = np.array([1.0, 1.0])
    x = (b+a)/2 + (b-a)/2 * zeta
    area = (b-a)/2 * np.sum(w * f(x))
    return area

f = lambda x: (2*x + 3/x) **2
a = 1
b = 2
my_gauss = gauss(f, a, b)
print("mygauss", my_gauss)

exact = quad(f, a,b)[0]
print("Exact", exact)
print("Error ", (exact - my_gauss) / exact * 100)
    
