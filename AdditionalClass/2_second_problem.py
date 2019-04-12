import numpy as np

a = np.array([[2, 1, -3], [1, 4, 2], [1, 2, 3]])

y = np.array([[1], [11], [11]])

print(np.linalg.solve(a, y))

#tranpose
print("Transpose")
a = np.array([1, 2, 3])
b = np.transpose(a)
print(a)
print(b)

a = np.matrix([1, 2, 3])
b = np.transpose(a)
# b = a.T
# also for transpose
print(b)

print("add , subtract, dot")

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(np.add(a, b));
print(np.subtract(a, b))

print(np.dot(a, b))


print("matmul")

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(np.matmul(a, b))

print("sqrt")
b = np.array([3, 4, 5])
print(np.sqrt(b))