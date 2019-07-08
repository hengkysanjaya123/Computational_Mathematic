# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:02:49 2019

@author: Hengky Sanjaya
"""

#2 Finding Roots


def f(x):
    return x**3 + 7*x**2 - 36

def f_deriv(x):
    return 3*x**2 + 14*x


def bisection(f, a , b ,e0):
    if(f(a) * f(b) >= 0):
        print("False intervals")
        return

    c = a
    while((b-a) >= e0):
        c = (a+b)/2

        if(f(c) == 0.0):
            break
        if(f(c)*f(a) < 0):
            b = c
        else:
            a = c

    return c

print(bisection(f, -4,-2, 0.05))


def bisection2(x1, x2):
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
            
        if(abs(mid - midPrev) <= 0.05):
            print(mid)
            break
    
bisection2(-4,-2)




def newtonRaphson_a( x ):
    h = f(x) / f_deriv(x)
    while abs(h) >= 0.05:
        h = f(x)/f_deriv(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    return x
    #print("The value of the root is : ",
    #                        "%.4f"% x)

print("Newton Rhapson algorithm : ",newtonRaphson_a(-3))


def newton(x1):
    xt = x1
        
    while(True):
        
        fxt = f(xt)
        fxt_deriv = f_deriv(xt)
        xt1 = float(xt - fxt / fxt_deriv)
        
        if(abs(xt1- xt) <= 0.05):
            return xt
            #print(xt)
            #print(xt1)
            break;
       
        #print("difference ",abs(xt1- x1))
        xt = xt1

print(newton(-3))








