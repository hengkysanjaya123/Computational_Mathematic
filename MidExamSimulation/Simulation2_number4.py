# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:35:14 2019

@author: Hengky Sanjaya
"""

import numpy as np

from scipy.integrate import *

def Gauss(f,a, b):
    zeta = np.array([-0.577350,0.577350])
    w = np.array([1.0, 1.0])
    x = (b+a)/2 + (b-a)/2 * zeta
    area = (b-a)/2 * np.sum(w * f(x))
    return area


f = lambda x : (2*x + 3/x)**2

a = 1
b = 2

area_scipy = quad(f, a, b)[0]
area_gauss = Gauss(f, a, b)
print("Area scipe " , area_scipy)
print("Area gauss ", area_gauss)