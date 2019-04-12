import matplotlib.pyplot as plt
import numpy as np

a = np.array([
    [12, 5, 7],
    [6, 13, 20]
])

b = np.array([
    [6, 5, 3],
    [2, 1, 7]
])

bTranspose = np.transpose(b)
aTranspose = np.transpose(a)

c = np.matmul(a, bTranspose)
print("C = A * B (Transpose)")
print(c)

d = np.matmul(aTranspose, b)
print("D = A (Transpose) * B")
print(d)


print("Determinant(C)")
dc = np.linalg.det(c)
print(dc)

print("Determinant(D)")
dd = np.linalg.det(d)
print(dd)


print("Inverse (C)")
ic = np.linalg.inv(c)
print(ic)

print("Inverse (D)")
if(dd == 0):
    print("No Solution")
else:
    id = np.linalg.inv(d)
    print(id)
