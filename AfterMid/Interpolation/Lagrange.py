from scipy.interpolate import interp1d, lagrange

# Lagrange method
x_array = [0, 2, 3, 4]
y_array = [7, 11, 28, 30]

n = 4
x = 3.5

total = 0
for l in range(0, n):
    #subtotal = l0, l1, l2, l3
    subtotal = 1
    for j in range(0, n):
        if (l != j):
            subtotal *= (x - x_array[j]) / (x_array[l] - x_array[j])
    # li * fi
    total += subtotal * y_array[l]

print(total)

print(lagrange(x_array,y_array))
f = interp1d(x_array, y_array)

x0 = 0
x1 = 2
x2 = 3
x3 = 4



y0 = 7
y1 = 11
y2 = 28
y3 = 30

l0 = (x- x1) * (x - x2) * (x-x3) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
l1 = (x - x0) * (x-x2) * (x-x3) / ((x1 - x0) * (x1 - x2) * (x1 - x3))

l2 = (x - x0) * (x-x1) * (x-x3) / ((x2 - x0) * (x2 - x1) * (x2-x3))

l3 = (x - x0) * (x-x1) * (x-x2) / ((x3- x0) * (x3 - x1) * (x3 - x2))


total = (y0 * l0) + (y1 * l1) + (y2 * l2) + (y3 * l3)
print(total)