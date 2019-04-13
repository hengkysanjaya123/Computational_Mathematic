import numpy as np
import math as m

from sympy import symbols, integrate

data = np.array([
                5.5, 1.1, 6.5, 4.9, 6.4,
                7.0, 1.5, 5.7, 5.9, 5.4,
                6.1, 1.2, 7.3, 6.1, 4.4,
            ])

#1 a)

mean = np.mean(data)
print(mean)

ssd = np.std(data, ddof=1)
print(ssd)

#1 b)
Q = np.percentile(data, [25, 50, 75])
print(Q)

#----------------------
#2

A = np.array([
    [6, 2, 0, 0, 0],
    [-1, 7, 2, 0, 0],
    [0, -2, 8, 2, 0],
    [0, 0, 3, 7, -2],
    [0, 0, 0, 3, 5]
])

b = np.array([
    [2],
    [-3],
    [4],
    [-3],
    [1]
])

#2 a)

x = np.linalg.solve(A, b)
print("Solution vector x ",x)

#2 b)
A_inverse = np.linalg.inv(A)
print("Inverse of matrix A ",A_inverse)

#2 c)
det_A = np.linalg.det(A)
print("Determinant of matrix A", det_A)

# test
transpose_A = np.transpose(A)
print("Transpose A : ",transpose_A)

#-------------------------
#3

#a)
def ln1_x(x, n):
    total = 0
    for i in range(0, n):
        value = m.pow(-x, i+1) / (i + 1)
        total = total + value
    return total

#b)
ln_1_8 = ln1_x(0.5, 8)
ln_1_16 = ln1_x(0.5, 16)
print("ln1_x 8 ", ln_1_8)
print("ln1_x 16", ln_1_16)

#c)
original = m.log(0.5)
print("ln(1-x) using math log ", original)

#d)
error_8 = original - ln_1_8
error_16 = original - ln_1_16
print("Error 8 ", error_8)
print("Error 16", error_16)
print("Percentage error 8 ", error_8 / original * 100, "%")
print("Percentage error 16 ", error_16 / original * 100, "%")

#------------------------------
#4

def f(x):
    return 2*x**4 + 6*x**3 - 2*x

def trapezoidal(a, b, n):
    h = (b-a)/n
    s = (f(a) + f(b)) * 0.5
    for i in range(1,n):
        s = s + f(a + i * h)

    return h * s

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

def simpson(a, b, n):
    h = (b-a)/ n
    x = a
    s = 0
    for i in range(1, n):
        x = x + h
        if(i%2==0):
            m = 2
        else:
            m = 4
        s = s + m * f(x)
    return (b-a) * (f(a) + s + f(b)) / (3*n)

trape = trapezoidal(0, 2, 4)
print("Trapezoidal ", trape)

simp = simpson1_3(0, 2, 4)
print("Simpson ", simp)

x = symbols('x')

exact_int = integrate(2*x**4 + 6*x**3 - 2*x, x)
exact = abs(exact_int.subs(x, 0) - exact_int.subs(x, 2))

print("Exact : ", float(exact))

error_trapezoid = exact - trape
error_simpson = exact - simp
print("Error Trapezoid : ", error_trapezoid)
print("Error simpson ", error_simpson)