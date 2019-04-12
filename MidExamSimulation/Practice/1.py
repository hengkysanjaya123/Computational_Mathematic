import numpy as np
import math

from sympy import *

data = [
        5.5, 1.1, 6.5, 4.9, 6.4,
        7.0, 1.5, 5.7, 5.9, 5.4,
        6.1, 1.2, 7.3, 6.1, 4.4,
        ]

print("1")
mean = np.mean(data)
print("\tA) Mean : ", mean)

ssd = np.std(data, ddof=1)
print("\tA) Sample Standard Deviation : ", ssd)

quantiles = np.percentile(data, [25, 50, 75])
print("\tB) Q1 , Q2, Q3 : ", quantiles)


print("--------------------------------------------------------------------------------------")
print("2")

A = [
        [6, 2, 0 , 0, 0],
        [-1, 7, 2, 0 ,0],
        [0, -2 ,8, 2, 0],
        [0, 0, 3, 7, -2],
        [0, 0, 0 , 3, 5]
]

b = [
        [2],
        [-3],
        [4],
        [-3],
        [1]
]

print("A) The solution of vector x : ", np.linalg.solve(A,b))
print("B) The inverse of the matrix A : ", np.linalg.inv(A))
print("C) The determinant of the matrix A : ", np.linalg.det(A))

print("--------------------------------------------------------------------------------------")
print("3")


def ln1_x(x,n):
    totalvalue = 0
    value = 0
    for i in range(0, n):
        # value = ((-x)**(i+1)) / (i+1)
        value = pow(-x, i + 1) / (i + 1)
        totalvalue += value
    return totalvalue


print("\tB) ln(1-x) with x = 0.5 using the 8 and 16 terms of the series")
firstvalue = ln1_x(0.5, 8)
second = ln1_x(0.5, 16)
print("\t\t8 : ", firstvalue)
print("\t\t16 : ", second)

logresult = math.log(0.5)
print("\tC) math log function ln(1-x)")
print("\t\tmath log : ", logresult)

print("\tD) relative error")
print("\t\tRelative errors of 8 terms : ", logresult - firstvalue)
print("\t\tRelative errors of 16 terms : ", logresult - second)



print("--------------------------------------------------------------------------------------")
print("4")

# https://en.wikipedia.org/wiki/Trapezoidal_rule
#http://hplgit.github.io/edu/py_vs_m/._numerical_programming_guide001.html
def f(x):
    return 2*x**4 + 6*x**3 - 2*x

def trapezoidal(a, b, n):
    h = (b-a) / float(n)
    s = (f(a) + f(b)) * 0.5
    for i in range(1, n):
        s = s + f(a + i * h)
    return h * s

#function from bimay
def trapezoid(a, b, n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range (1,n):
        x = x + h
        s = s + f(x)
    return (b-a)*(f(a)+2*s+f(b))/(2*n)

print(trapezoidal(0, 2, 4))
print(trapezoid(0,2,4))
# compare the result here
#https://www.integral-calculator.com/

#https://planetmath.org/codeforsimpsonsrule

# function from bimay
def simpson1_3(a, b, n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range (1,n):
        x = x + h
        if i % 2 == 0:
            m = 2
        else:
            m = 4
        s = s + m*f(x)
    return (b-a)*(f(a)+s+f(b))/(3*n)

n = 4
a = 0
b = 2

x = symbols('x')
exact_int = integrate(2*x**4 + 6*x**3 - 2*x, x)
exact = abs(exact_int.subs(x,a) - exact_int.subs(x,b))

print("Exact Integral Value : ", float(exact))
print("Approx simpson1/3 : ", simpson1_3(a, b, n))
print("Approx trapezoid : ", trapezoid(a, b, n))