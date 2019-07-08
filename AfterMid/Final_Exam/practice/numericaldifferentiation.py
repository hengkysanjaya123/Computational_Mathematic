# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:38:34 2019

@author: Hengky Sanjaya
"""

# numerical differentiation

def f(x):
    return x**4 - 3*x**3 + 6*x**2 - 10 *x - 9

def f_deriv1(x):
    return 4*x**3 - 9*x**2 + 12*x - 10

def f_deriv2(x):
    return 12*x**2 - 18*x + 12

def f_deriv_central(x, h , level):
    if(level == 1):
        return (f(x+h) - f(x-h)) / 2*h
    elif(level == 2):
        return (f(x+h) - 2*f(x) + f(x-h)) / h**2
    else:
        return 0
    
    
x = 1
h = 0.5
h1 = 0.25
h2 = 0.125

print("First 0.5", f_deriv_central(x, h, 1))
print("First 0.25", f_deriv_central(x, h1, 1))
print("First 0.125", f_deriv_central(x, h2, 1))

print("Second 0.5", f_deriv_central(x, h, 2))
print("Second 0.25", f_deriv_central(x, h1, 2))
print("Second 0.125", f_deriv_central(x, h2, 2))


print("First Exact", f_deriv1(x))
print("Second Exact", f_deriv2(x))