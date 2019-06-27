# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:41:47 2019

@author: Hengky Sanjaya
"""

import numpy as np
from sympy import Symbol, Derivative
import matplotlib.pyplot as plt


f = lambda x: np.e ** (-x)

def f_deriv(value):
    x = Symbol('x')
    deriv = Derivative(f(x),x)
    return deriv.doit().subs({x:value})

def f_diff_forward(x,h, level):
    if(level == 1):
        return (f(x+h) - f(x)) / h
    elif(level == 2):
        return (f(x) - 2*f(x+h) + f(x+2*h)) / h**2
    elif(level == 3):
        return (-1*f(x) +3 *f(x+h) -3 * f(x+2*h) + f(x+3*h)) / h**3
    elif(level == 4):
        return (f(x) + -4 * f(x+h) + 6 * f(x+2*h) -4*f(x+3*h) + f(x+4*h)) / h**4
    else:
        return 0

def f_diff_2ndForward(x,h,level):
    if(level == 1):
        return (-3*f(x) + 4*f(x+h) -1*f(x+2*h)) /2*h
    elif(level == 2):
        return 2*f(x) -5*f(x+h) + 4*f(x+2*h) -1*f(x+3*h)
    else:
        return 0

def f_diff_backward(x,h,level):
    if(level == 1):
        return (f(x)-f(x-h)) / h
    elif(level == 2):
        return (f(x-2*h) -2 *f(x-h) + f(x)) / h**2
    elif(level == 3):
        return (-1 * f(x-3*h) + 3*f(x-2*h) -3 *f(x-h) + f(x)) / h**3
    elif(level == 4):
        return (f(x-4*h) -4*f(x-3*h) + 6*f(x-2*h) - 4*f(x-h) + f(x)) / h**4
    else:
        return 0

def f_diff_central(x, h, level):
    if(level == 1):
        return (f(x+h) - f(x-h))/ 2*h
    elif(level == 2):
        #return (f_diff_forward(x,h, 1) - f_diff_backward(x,h))  /h
        return (f(x+h) -2*f(x) + f(x-h)) / h**2
    elif(level == 3):
        return (-1*f(x-2*h) + 2*f(x-h) -2*f(x+h) + f(x+2*h)) / 2*h**3
    elif(level == 4):
        return (f(x-2*h) -4*f(x-h) + 6*f(x) -4*f(x+h) + f(x+2*h)) / h**4
    else:
        return 0
    

    
x = 1
n = 10

h_data = np.linspace(0.00001, 0.64,n)

f_forward = []
f_forward_2 = []
f_forward_3 = []
f_forward_4 = []

f_2ndForward = []
f_2ndForward_2 = []

f_central = []
f_central_2 = []
f_central_3 = []
f_central_4 = []

f_backward = []
f_backward_2 = []
f_backward_3 = []
f_backward_4 = []

for h in h_data:
    f_2ndForward.append(f_diff_2ndForward(x,h,1))
    f_2ndForward_2.append(f_diff_2ndForward(x,h,2))
    
    f_forward.append(f_diff_forward(x,h,1))
    f_forward_2.append(f_diff_forward(x,h,2))
    f_forward_3.append(f_diff_forward(x,h,3))
    f_forward_4.append(f_diff_forward(x,h,4))
    
    f_central.append(f_diff_central(x,h,1))
    f_central_2.append(f_diff_central(x,h,2))
    f_central_3.append(f_diff_central(x,h,3))
    f_central_4.append(f_diff_central(x,h,4))
    
    f_backward.append(f_diff_backward(x, h,1))
    f_backward_2.append(f_diff_backward(x, h,2))
    f_backward_3.append(f_diff_backward(x, h,3))
    f_backward_4.append(f_diff_backward(x, h,4))



print("Forward 1st",f_forward)
print("\n")
print("forward 2nd",f_forward_2)
print("\n")
print("forward 3rd",f_forward_3)
print("\n")
print("forward 4th",f_forward_4)
print("\n")

print("2ndForward 1st",f_2ndForward)
print("\n")
print("2ndforward 2nd",f_2ndForward_2)
print("\n")

print("Central 1st",f_central)
print("\n")
print("Central 2nd",f_central_2)
print("\n")
print("Central 3rd",f_central_3)
print("\n")
print("Central 4th",f_central_4)
print("\n")


print("Backward 1st",f_backward)
print("\n")
print("Backward 2nd",f_backward_2)
print("\n")
print("Backward 3rd",f_backward_3)
print("\n")
print("Backward 4th",f_backward_4)
print("\n")

print("Actual ", f_deriv(x))


x_values = np.linspace(0, 100, 10)

plt.style.use('ggplot')

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("Forward")
ax.plot(x_values, f_forward,label='Forward 1st')
ax.plot(x_values, f_forward_2,label='Forward 2nd')
ax.plot(x_values, f_forward_3,label='Forward 3rd')
ax.plot(x_values, f_2ndForward, label='2nd Forward 1st')
ax.plot(x_values, f_2ndForward_2, label='2nd Forward 2st')
#ax.plot(x_values, f_forward_4,label='Forward 4')
ax.plot(x_values, f_deriv(x)*np.ones(10), label='Actual')
ax.legend()


fig2 = plt.figure(2)
plt.clf()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.set_title("Backward")
ax2.plot(x_values, f_backward,label='Backward 1st')
ax2.plot(x_values, f_backward_2,label='Backward 2nd')
ax2.plot(x_values, f_backward_3,label='Backward 3rd')
#ax2.plot(x_values, f_backward_4,label='Backward 4')
ax2.legend()

fig3 = plt.figure(3)
plt.clf()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.set_title("Central")
ax3.plot(x_values, f_central,label='Central 1st')
ax3.plot(x_values, f_central_2,label='Central 2nd')
ax3.plot(x_values, f_central_3,label='Central 3rd')
#ax2.plot(x_values, f_backward_4,label='Backward 4')
ax3.legend()
