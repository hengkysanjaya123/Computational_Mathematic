# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:48:57 2019

@author: Hengky Sanjaya
"""

import numpy as np
from scipy.integrate import *

def Gauss(f, a, b):
    zeta = np.array([0.774597 , 0, -0.774597])
    w = np.array([0.555556,0.888889, 0.555556])
    
    x = (b+a)/2 + (b-a)/2 * zeta
    area = (b-a)/2 * np.sum(w * f(x))
    return area

f = lambda x: (2+ np.sin(x))

a = 0
b = np.pi / 2

area_scipy = quad(f, a, b)[0]
area_gauss = Gauss(f, a, b)

print("Area scipy ", area_scipy)
print("Area gauss ", area_gauss)