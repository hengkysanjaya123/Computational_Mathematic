import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fact
from scipy.integrate import odeint, quad
plt.style.use('ggplot')

#
# Problem 1
# 
print('========= PROBLEM 1 ==========')
print('*** See Figure 100')

data = np.array([12.5, 11.4, 15.7, 13.1, 12.9, 14.1]) # Sample data
mean = data.mean()                                    # Sample mean
std = np.std(data, ddof = 1)                          # Sample standard deviation
q = np.percentile(data, [25, 50, 75])                 # Quantiles
n = len( data )

fig = plt.figure(100); plt.clf()
ax = fig.add_subplot(2,3,1)
ax.plot( np.ones( n ), data, 'o')
ax.errorbar(1.2, mean, std, capsize = 5)
ax.plot(1.2, mean,"sk")
ax.boxplot(data , positions = [0.8])
ax.set_xlim( [0, 2] )
ax.set_ylim( [10, 17])
ax.set_title('Problem 1')


# 
# Problem 2
#
# https://socratic.org/questions/how-do-you-find-the-maclaurin-series-of-f-x-cos-x-2
print('')
print('========= PROBLEM 2 ==========')
def mycos(x, n):
    total = 0
    for i in range( n ):
        # total = total + (-1)**i * (8*x)**(2*i) / fact(2*i)
        total = total + (-1)**i * (x)**(2*i) / fact(2*i)
    return total

x = 3/8*np.pi; n = 20
print('Numpy result = {0}'.format( np.cos(8.0*x) ) )
print('Mycos result = {0}'.format( mycos(x, n) ) )



#
# Problem 3
#
print('')
print('========= PROBLEM 3 ==========')
A = np.array([[3.0, 1.0, 0.0, 0.0],
              [2.0, 3.0, 2.0, 0.0],
              [1.0, 2.0, 4.0, 1.0],
              [0.0, 1.0, 1.0, 2.0]])
b = np.matrix([ [1.0], [1.0], [1.0], [1.0] ] )
x = np.linalg.solve(A, b)               
print( 'The solution vector x = {0}'.format(x.transpose()) )
print( 'The det(A) = {0}'.format( np.linalg.det(A)))
print( 'The norm(b) = {0}'.format( np.linalg.norm(b)))


#
# Problem 4
#
# http://www.arpnjournals.org/jeas/research_papers/rp_2017/jeas_0717_6155.pdf
print('')
print('========= PROBLEM 4 ==========')
def rk6(f,y0,x):
    h = x[1] - x[0]; n = len(x)
    y = np.zeros(n)
    y[0] = y0
    s21 = np.sqrt(21.0)
    for i in range(n - 1):
        k1 = h * f( x[i], y[i] )
        k2 = h * f( x[i] + h, y[i] + k1 )
        k3 = h * f( x[i] + h/2, y[i] + (3*k1 + k2)/8 )
        k4 = h * f( x[i] + 2*h/3, y[i]+ (8*k1 + 2*k2 + 8*k3)/27)
        k5 = h * f( x[i] + (7 - s21)*h/14, y[i] + (  3*(3*s21 - 7)*k1 - 8*(7 - s21)*k2 + 48*(7 - s21)*k3 - 3*(21 - s21)*k4)/392)        
        k6 = h * f( x[i] + (7 + s21)*h/14, y[i] + ( -5*(231 + 51*s21)*k1 - 40*(7 + s21)*k2 - 320*s21*k3 + 3*(21 + 121*s21)*k4 + 392*(6 + s21)*k5 )/1960)
        k7 = h * f( x[i] + h, y[i] + ( 15*(22 + 7*s21)*k1 + 120*k2 + 40*(7*s21 - 5)*k3 - 63*(3*s21 - 2)*k4 - 14*(49 + 9*s21)*k5 + 70*(7 - s21)*k6)/180)
        y[i+1] = y[i] + ( 9*k1 + 64*k3 + 49*k5 + 49*k6 + 9*k7 )/180
    return y


f = lambda x,y : np.exp(-x) + np.sin(y)
y0 = np.array([1]); x = np.linspace(0.0, 1.0, 11)
y_rk6 = rk6(f, y0, x)
y_python = odeint(f, y0, x)
ax = fig.add_subplot(2,3,2); 
ax.plot(x, y_rk6, label = 'RK6')
ax.plot(x, y_python, label = 'Scipy')
ax.legend()

print('*** See Figure 100. I guess something is wrong with the formulas.')


#
# Problem 5
#
# https://pomax.github.io/bezierinfo/legendre-gauss.html
print('')
print('========= PROBLEM 5 ==========')

def Gauss( f, a, b):
    zeta  = np.array([-0.774597, 0.0, 0.774597])
    w = np.array([0.555556, 0.888889, 0.555556])
    x = (b + a)/2 + (b-a) / 2 * zeta
    area = (b - a)/2*np.sum( w * f(x) )
    return area

f = lambda x: 2 + np.sin(x)
a = 0.0; b = np.pi/2

area_scipy = quad(f, a, b)[0]
area_Gauss = Gauss(f, a, b)
print ('Area by scipy = {0}'.format( area_scipy) )
print ('Area by Gaussian Quadrature = {0}'.format( area_Gauss) )


# From: Millen DwiPutra <Millen-putra@hotmail.com> 
# Sent: Friday, April 12, 2019 2:00 PM
# To: Fergyanto E. Gunawan <fgunawan@binus.edu>
# Subject: Pre-MidTest Answer

# Dear Mr. Gunawan,

#              I am Millen from L2AC, as you mentioned before, you would like to share us the pre-midtest answer for computational mathematics. Can we have the answer as soon as possible, so, we can prepare more for it.

# Thanks,
# Millen
