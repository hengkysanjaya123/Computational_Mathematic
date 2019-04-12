import numpy as np
import math as m

def f(x):
    return 2*x**4 + 6*x**3 -2*x


def trapezoid(a, b, n):
    h = (b - a) / float(n)
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n, 1):
        s = s + f(a + i * h)
    return h * s

def simpson1_3(a, b, n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range (1, n):
        x = x+h
        if i % 2 == 0:
            m = 2
        else:
            m = 4
        s = s + m*f(x)
    return (b-a)*(f(a) + s + f(b))/(3*n)

print (trapezoid(0,2,4))
print (simpson1_3(0, 2, 4))

