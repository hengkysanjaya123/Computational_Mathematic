# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:31:53 2019

@author: Hengky Sanjaya
"""

# numerical differentiation

def f(x):
    return x**4 - 3*x**3 + 6*x**2 - 10*x - 9


def f_deriv_central(x, h, level):
    if(level == 1):
        return (f(x+h) - f(x-h)) / 2*h
    elif(level == 2):
        return (f(x-h) -2*f(x) + f(x+h)) / h**2 
    else:
        return 0
    

h = 0.5
h2 = 0.25
h3 = 0.125


print("First h = 0.5", f_deriv_central(1, h, 1))
print("First h = 0.25", f_deriv_central(1, h2, 1))
print("First h = 0.125", f_deriv_central(1, h3, 1))


print("Second h = 0.5", f_deriv_central(1, h, 2))
print("Second h = 0.25", f_deriv_central(1, h2, 2))
print("Second h = 0.125", f_deriv_central(1, h3, 2))