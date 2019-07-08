# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:13:28 2019

@author: Hengky Sanjaya
"""

#rootfinding

def f(x):
    return x**3 + 7*x**2 - 36

def f_deriv(x):
    return 3*x**2 + 14*x

a = -4 #lower
b = -2 #upper
ea = 0.05

def bisection(f, a, b, ea):
    if(f(a) * f(b) >= 0):
        print("False Interval")
        return
    
    c = a
    while(abs(b-a) >= ea):
        c = (a+b)/2
        
        if(f(c) == 0.0):
            break
        if(f(c)*f(a) < 0):
            b = c
        else:
            a = c
    return c

print(bisection(f,a,b,ea))


def newtonRaphson(x):
    h = f(x) / f_deriv(x)
    
    while(abs(h) >= 0.05):
        h = f(x) / f_deriv(x)
        
        x = x - h
    
    return x

print(newtonRaphson(-3))