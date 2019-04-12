import numpy as np
print("Number 4")


def y(x):
    # Declaring the function
    # f(x) = 1/(1+x*x)
    return 1 / (1 + x * x)


# Function to evalute the value of integral
def trapezoidal(a, b, n):
    h = (b - a) / n

    s = (y(a) + y(b))

    i = 1
    while i < n:
        s += 2 * y(a + i * h)
        i += 1

    return (h / 2) * s


def simps(f, a, b, n=4):
    if n % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


x0 = 0
xn = 2

n = 4
check = trapezoidal(x0, xn, n)
print("Value of integral is ",
      "%.4f" % trapezoidal(x0, xn, n))

manual_value = 32.8

answer = ((manual_value-check)/manual_value)*100
answer2 = simps(lambda x : 2*x**4+6*x**3, 0, 2, 4)
answer2 = ((answer2-manual_value)/manual_value)*100
print("The relative error is (Using Trapezoidal rule)", answer)
print("The relative error is (Using Simpson rule)", answer2)