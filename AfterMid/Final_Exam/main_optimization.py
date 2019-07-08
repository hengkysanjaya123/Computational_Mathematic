# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:57:52 2019

@author: Hengky Sanjaya
"""

#optimization
import numpy as np


def obj(x):
    x0 = x.item(0)
    print("x0: ", x0)
    x1 = x.item(1)
    print("x1: ",x1)
    f = 2*x0*x1 + 2*x0 + x0**2 - 2*(x1**2)
    g = np.array([
                    [2*x1 + 2 + 2*x0, 2*x0 - 4*x1]
                 ])
    return f,g


def steepest(x):
    #initial_point = np.array([x])
    a = 0.1
    iteration = 0
    for i in range(0, 10):
        f, g = obj(x)
        s = -g
        
        print("fx: " , f)
        print("iteration ",iteration ,"\n")
        iteration+=1
        x = x + a * s
        #initial_point = np.vstack((initial_point,x))
        
    #return initial_point


x = np.array([0.5, 1.0])
steepest(x)