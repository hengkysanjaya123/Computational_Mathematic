import numpy as np
from scipy.linalg import solve
A = np.array([[6, 2, 0, 0, 0],
    [-1, 7, 2, 0, 0],
    [0, -2, 8, 2, 0],
    [0, 0, 3, 7, -2],
    [0, 0, 0, 3, 5]])

B = np.array([[2],
             [-3],
             [4],
             [-3],
             [1]])

X = solve(A,B)

print(X)
inverse = np.linalg.inv(A)
print(inverse)
determinant = np.linalg.det(A)
print(determinant)