# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:42:32 2019

@author: Hengky Sanjaya
"""

from sympy import Symbol, Derivative


def f(x):
    return x**3 - x**2- 10*x - 8

def f_deriv(value):
    x = Symbol('x')
    deriv = Derivative(f(x),x)
    return deriv.doit().subs({x:value})


def newton(x1):
    xt = x1
        
    while(True):
        fxt = f(xt)
        fxt_deriv = f_deriv(xt)
        xt1 = float(xt - fxt / fxt_deriv)
        
        if(abs(xt1- xt) <= 0.00000000001):
            print(xt)
            #print(xt1)
            break;
       
        print("difference ",abs(xt1- x1))
        xt = xt1
        
        
newton(2.75)