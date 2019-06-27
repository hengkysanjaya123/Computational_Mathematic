# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:54:32 2019

@author: Hengky Sanjaya
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import math

def f(x):
    return (x/2)**2 - math.sin(x)

def f2(x):
    return (x**4) - 3*(x**3) + 4*x - 5


def f_deriv(f,value):
    return derivative(f,value)
    

def newton(f,x1):
    xt = x1
        
    while(True):
        fxt = f(xt)
        fxt_deriv = f_deriv(f,xt)
        xt1 = float(xt - fxt / fxt_deriv)
        
        if(abs(xt1- xt) <= 0.00000000001):
            print(xt)
            #print(xt1)
            break;
       
        #print("difference ",abs(xt1- x1))
        xt = xt1
        

def bisection(f,x1, x2):
    xs = x1
    xe = x2
    fxs = f(xs)
    fxe = f(xe)
    
    if((fxs > 0 and fxe > 0 ) or (fxs < 0 and fxe < 0 )):
        print("Wrong initial value")
        return None
    
    
    midPrev = 0
    mid = 0
    while(True):
        midPrev = mid
        mid = (xs + xe) /2
        fmid = f(mid)
        #print("fmid ",fmid)
       
        if(fxs < 0):
            if(fmid > 0):
                xe = mid
            elif(fmid < 0):
                xs = mid
        elif(fxs > 0):
            if(fmid > 0):
                xs = mid
            elif(fmid < 0):    
                xe = mid
            
        if(abs(mid - midPrev) <= 0.01):
            print(mid)
            break
    
    
print(f(0.5))
print(f(2.1))

bisection(f,0.5, 2.1)
bisection(f2, 1 , 3)
newton(f, 2)
newton(f2, 3)
    
#x = np.arange(0, np.pi, 0.05)

#y = []
#for i in x:
#    y.append(f2(i))

#print(x)
#print(y)
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')
#plt.plot(x, y)



