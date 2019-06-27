# Linear Interpolation for Depth = -7.5

x_array = [-6, -7, -8,-9]
y_array = [18.2, 17.6, 11.7, 9.9]


x0 = -7
x1 = -8
b0 = 17.6
td1 = 11.7
def getB1(d, b0, d0, td1):
    # td1 = b0 + b1 * (d - d0)
    return (-1 *b0 + td1) / (d-d0)

def linear_interpolation(D, b0):
    return b0 + getB1(x1,b0, x0, td1) * (D - x0)


print(linear_interpolation(-7.5, 17.6))