import numpy as np


a = np.array([[2, 1, -3], [1, 4, 2], [1, 2, 3]])
# a = np.array([[0,0,0], [0,0,0], [0,0,0]])

y = np.array([[1], [11], [11]])

det = np.linalg.det(a)
if(det == 0):
    print("No Solution")
else:
    print(np.linalg.solve(a, y))

