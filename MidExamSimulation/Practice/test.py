# def Trapezoidal(f, a, b, n):
#     h = (b-a)/float(n)
#     s = 0.5*(f(a) + f(b))
#     for i in range(1,n,1):
#         s = s + f(a + i*h)
#     return h*s
#
# from math import exp  # or from math import *
# def g(t):
#     return exp(-t**4)
#
#
# print (Trapezoidal(g,0,2,4))

# b = 5
# a = 8
# n = 5
# h = (b-a)/ n
# print(h)

#
# from math import *
# def f(x):
#   #function to integrate
#   return sin(x)
#
# def simpson_rule(a,b):
#   #Approximation by Simpson's rule
#   c=(a+b)/2.0
#   h=abs(b-a)/2.0
#   return h*(f(a)+4.0*f(c)+f(b))/3.0
#
# # Calculates integral of f(x) from 0 to 1
# print(simpson_rule(0,1))



#
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, \
#    label='parametric curve')
# ax.legend()
# plt.show()
#
# np.cos()



import numpy as np
#
# Problem 5
#
from scipy.integrate import quad

print('')
print('========= PROBLEM 5 ==========')

def Gauss( f, a, b):
    zeta  = np.array([-0.774597, 0.0, 0.774597])
    w = np.array([0.555556, 0.888889, 0.555556])
    x = (b + a)/2 + (b-a)/2*zeta
    area = (b - a)/2*np.sum( w * f(x) )
    return area

f = lambda x: 2 + np.sin(x)
a = 0.0; b = np.pi/2

area_scipy = quad(f, a, b)[0]
area_Gauss = Gauss(f, a, b)
print ('Area by scipy = {0}'.format( area_scipy) )
print ('Area by Gaussian Quadrature = {0}'.format( area_Gauss) )