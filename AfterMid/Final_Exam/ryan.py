import numpy as np
import math

#no 1
print("Number 1")

p = np.array([44 * math.pi/180 , 46 * math.pi/180])
q = np.ones(len(p))

for i in range(len(p)):
    q[i] = math.tan(p[i])



def newton_interpolation(p,q,p1):
    b0 = q[0]
    b1 = (q[1] - q[0])/(p[1] - p[0])

    order_1 = b0
    order_2 = b0 + b1 * (p1-p[0])

    return order_2

print("Second order Newton's interpolation method , tan 45 estimated: ", newton_interpolation(p,q,45*math.pi/180))



def larange_interpolation(p,q,p1):

    b0 = q[0]* ((p1-p[1]) / (p[0]-p[1]))
    b1 = q[0]* ((p1-p[0]) / (p[1]-p[0]))

    return b0+b1

print("Second order larange interpolation method , tan 45 estimated: ", larange_interpolation(p,q,45*math.pi/180))
exact = 1
newton = round(abs(((exact - newton_interpolation(p,q,45*math.pi/180))/exact) * 100),3)
larange = round(abs(((exact - larange_interpolation(p,q,45*math.pi/180))/exact) * 100),3)

print("Relative errors : Newton : ",newton,"\n Larange : ", larange)
print("Hence, Newton interpolation method is the best estimation")




#no 2
print("Number 2")


def f(x):
    return x**3 + 7*x**2 -36



def derivf(x):
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

print("Bisection algorithm : ", bisection(f,-4,-2,0.05))





# Function to find the root
def newtonRaphson_a( x ):
    h = f(x) / derivf(x)
    while abs(h) >= 0.05:
        h = f(x)/derivf(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",
                             "%.4f"% x)


print("Newton Rhapson algorithm : ",newtonRaphson_a(x=-3))

    



print("Number 3")

def f3(x):
    return x**4 - 3 * x**3 + 6 * x**2 - 10 * x - 9



def rk4(f,x0,y0,n,h):
    x = []
    x.append(x0)
    y = []
    y.append(y0)