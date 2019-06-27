# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:21:58 2019

@author: Hengky Sanjaya
"""



def f(x):
    return x**3 - x**2- 10*x - 8


def bisection(x1, x2):
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
        print("fmid ",fmid)
       
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
    

    
bisection(3.75, 5.00)
bisection(5.00, 3.75)




