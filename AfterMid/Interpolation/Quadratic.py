from scipy.interpolate import CubicSpline

x_array = [-6, -7, -8,-9]
y_array = [18.2, 17.6, 11.7, 9.9]

n = 4
x = -7.5

total = 0
for l in range(0, n):
    #subtotal = l0, l1, l2, l3
    subtotal = 1
    for j in range(0, n):
        if (l != j):
            subtotal *= (x - x_array[j]) / (x_array[l] - x_array[j])
    # li * fi
    total += subtotal * y_array[l]

print("Langrange : ", total)


def quadratic(BASE,x,y, value):
    b0 = y[BASE]
    b1 = (y[BASE+ 1] - b0) / (x[BASE+1] - x[BASE+0])
    b12 = (y[BASE+2] - y[BASE+1]) / (x[BASE+2] - x[BASE+1])
    b2 = (b12 - b1) / (x[BASE+2] - x[BASE+0])
    # print("b0", b0)
    # print("b1", b1)
    # print("b2", b2)
    return b0 + b1 * (value - x[BASE+0]) + b2 * (value - x[BASE+0])*(value - x[BASE+1])


q = quadratic(1, x_array, y_array, -7.5)
print("Quadratic : ",q)


def cubic(BASE,x,y, value):
    b0 = y[BASE+0]
    b1 = (y[BASE+1] - b0) / (x[BASE+1] - x[BASE+0])
    b12 = (y[BASE+2] - y[BASE+1]) / (x[BASE+2] - x[BASE+1])
    b13 = (y[BASE+3] - y[BASE+2]) / (x[BASE+3] - x[BASE+2])
    b2 = (b12 - b1) / (x[BASE+2] - x[BASE+0])
    b22 = (b13 - b12) / (x[BASE+3] - x[BASE+1])
    b3 = (b22 - b2) / (x[BASE+3] - x[BASE+0])

    return b0 + b1 * (value - x[BASE+0]) + b2 * (value - x[BASE+0])*(value - x[BASE+1]) + b3 * (value - x[BASE+0]) * (value - x[BASE+1]) * (value - x[BASE+2])

c = cubic(0, x_array, y_array, -7.5)
print("Cubic Interpolation :",c)

# x_points = [ 0, 1, 2, 3, 4, 5]
# y_points = [12,14,22,39,58,77]

# tck = interpolate.splrep(x_points, y_points)
# tck = interpolate.splrep(x_array, y_array)
# print(interpolate.splev(-7.5, tck))

print("Error quadratic & Lagrange: " , abs(q - total))
print("Error cubic & Lagrange: " , abs(c - total))


