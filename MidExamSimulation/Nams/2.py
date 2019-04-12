import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sp

# Number 1
x = []
data = ([5.5, 1.1, 6.5, 4.9, 6.4, 7.0, 1.5, 5.7, 5.9, 5.4, 6.1, 1.2, 7.3, 6.1, 4.4])
minimum = np.min(data)
maximum = np.max(data)
median = np.median(data)
arrayInfo = [minimum, maximum, median]
for i in range(len(data)):
    x.append(1)

plt.boxplot(data, positions=[1.3])
plt.scatter(x, data)
plt.errorbar(1.6, arrayInfo, marker="o")
plt.xticks([1, 1.3, 1.6], ["Data", "Error Bar", "Box Plot"])
plt.title("Sample Data")
# plt.errorbar(2, [arrayInfo], marker="o")
plt.show()

# Number 2.a

matrixA = np.array([[6, 2, 0, 0, 0], [-1, 7, 2, 0, 0], [0, -2, 8, 2, 0], [0, 0, 3, 7, -2], [0, 0, 0, 3, 5]])
matrixB = np.array([[2], [-3], [4], [-3], [1]])

print("======================================")
print("======================================")
print("Number 2. a")
print(np.transpose(matrixA))
print(np.transpose(matrixB))

# Number 2.b

print("Number 2. b")
sol = np.linalg.solve(matrixA, matrixB)
print(np.linalg.norm(sol))

# Number 3

print("======================================")
print("======================================")


def taylor_1(x, n):
    ans = 0
    for i in range(1, n+1):
        ans = x**i + ans

    return 1+ans


def main():
    print("3. b")
    print("if n = 5, answer is ", taylor_1(0.1, 5))
    print("n = 10, answer is ", taylor_1(0.1, 10))
    print("3. c")
    original_value = 1 / (1 - 0.1)
    error = ((original_value-taylor_1(0.1, 5)) / original_value) * 100
    error1 = ((original_value-taylor_1(0.1, 10)) / original_value) * 100
    print("The relative error (if compared with value in b where n = 5 ) ", error)
    print("The relative error (if compared with value in b where n = 10 ) ", error1)


main()

# Number 4

print("======================================")
print("======================================")

print("Number 4")
# ALTERNATIVE METHOD USING INBUILT FUNCTION
# f = lambda x: (2*x + 3/x)**2
original_val = 155/6
# print(sp.quadrature(f, 1, 2))
# val_1 = sp.quadrature(f, 1, 2)
# val_2 = val_1[0]

# error2 = ((original_val-val_2)/original_val)*100
# print("The error is ", error2)

conv = (2-1)/2
conp = (2+1)/2
c1 = -0.577350
c2 = 0.577350


def f(x):
    return (2*x+3/x)**2


test = conv*f(conv*c1+conp)+conv*f(conv*c2+conp)
ans2 = ((original_val-test)/original_val)*100
print("The answer is", ans2)