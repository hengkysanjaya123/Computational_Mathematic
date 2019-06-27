# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:39:03 2019

@author: Hengky Sanjaya
"""
import math


def goldenSectionSearch(f, lower, upper):    
    r = (math.sqrt(5) - 1) / 2
    d = r * (upper - lower)
    
    x1 = lower + d
    x2 = upper - d
    
    
    while(abs(x1-x2) > 0.00001):
       
        if(f(x1) > f(x2)):
            lower = x2
            x2 = x1
            x1 = lower + (r * (upper - lower))
        elif(f(x2) > f(x1)):
            upper = x1
            x1 = x2
            x2 = upper - (r * (upper - lower))
    print(x1)
            
# 1 -------------------------------------------
xl = -1
xu = 1.5
func = lambda x : x**2
 
goldenSectionSearch(func, xl, xu)


 