# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:50:07 2019

@author: Hengky Sanjaya
"""
import numpy as np

x = np.array([0.5, 1.0])


def obj(x):
    x0 = x.item(0)
    print("x0  : ", x0)
    x1 = x.item(1)
    print("x1  : ", x1)
    
    f = 2*x0*x1 + 2*x0 + x0**2 - 2*x1**2
    
    g = np.array([2*x1 + 2 + 2*x0, 2*x0 - 4*x1])
    return f,g

def steepest(x):
    a = 0.1
    
    for i in range(0,10):
        f, g = obj(x)
        s = -g
        
        print("F(x) : " , f)
        
        x = x + a * s
        

steepest(x)
        
        
        