# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:27:30 2019

@author: Hengky Sanjaya
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2 + 3*x + 5

# =============================================================================
# a = 0;b = 5;N = 100;n = 10
# 
# x = np.linspace(a, b, N+1)
# y = f(x)
# dx = (b-a)/N
# 
# X = np.linspace(a, b, n*N+1)
# Y = f(X)
# plt.plot(X,Y)
# 
# area = 0
# 
# for i in range(N):
#     xs = [x[i], x[i], x[i+1], x[i+1]]
#     area = area + (dx/2) * (f(x[i]) + f(x[i+1]))
#     ys = [0, f(x[i]), f(x[i+1]), 0]
#     plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
# 
# plt.title("Trapezoid Rule, N = {}".format(N))
# plt.show()
# print("Areaa" , area)
# 
# 
# 
# x = np.linspace(a, b,N+1)
# y = f(x)
# 
# X = np.linspace(a, b, n* N+1)
# Y = f(X)
# plt.plot(X,Y)
# 
# 
# 
# def trapezoidal(f, a, b, n):  
#     h = (b-a)/n
#     s = (f(a) + f(b)) * 0.5
#     for i in range(1,n):
#         #xs = [x[i], x[i], x[i+1], x[i+1]]
#         #ys = [0, f(x[i]), f(x[i+1]), 0]
#         #plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)    
#         s = s + f(a + i * h)
#         
#     #plt.show()
# 
#     return h * s
# 
# 
# #print(trapezoidal(a, b, N))
# 
# 
# a = 1
# b = 5
# n = 100
# f = lambda x: 2*x**3 + 4*x**2 +5
# print(trapezoidal(f, a , b, n))
# 
# a = 2
# b = 10
# n = 100
# f = lambda x: 3*(x-5)**2 + 3*x
# print(trapezoidal(f, a, b,n))
# 
# a = -2
# b = 8
# n = 100
# f = lambda x: 3*(x+5)**2 + 3*(x-5)
# print(trapezoidal(f, a, b,n))
# =============================================================================

x = np.linspace(a, b, n+1)
y = f(x)
plt.plot(x, y)


def trapezoid(f, a, b, n):
    h = (b-a)/n
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        xs = [x[i], x[i], x[i+1], x[i+1]]
        ys = [0, f(x[i]), f(x[i+1]), 0]
        plt.fill(xs, ys, 'b', alpha=0.3)
        s = s + f(a + i * h)
    return h * s

plt.tight_layout(0)

a = -2
b = 8
n = 100

print(trapezoid(f, a, b, n))
    

    
    
    

    
    
    
    
    
    
    
    
    
    
