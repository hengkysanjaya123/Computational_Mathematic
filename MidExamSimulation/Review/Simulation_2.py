import numpy as np

# --------------------------------
# 2

A = np.array([
    [6, 2, 0, 0, 0],
    [-1, 7, 2, 0, 0],
    [0, -2, 8, 2, 0],
    [0, 0, 3, 7, -2],
    [0, 0, 0, 3, 5]
])

b = np.array([
    [2],
    [-3],
    [4],
    [-3],
    [1]
])

#2 a)
transpose_A = np.transpose(A)
transpose_b = np.transpose(b)
print("Transpose A", transpose_A)
print("Transpose b", transpose_b)

#2 b)
x = np.linalg.solve(A, b)
norm = np.linalg.norm(x)
print("Euclidean norm of vector x ", norm)

#---------------------------
#3 a)

def taylor_1(x,n):
    a = 0
    for i in range(1, n + 1):
        a = a + x**i
    return 1 + a

#3 b)
tay_5 = taylor_1(0.1 , 5)
tay_10 = taylor_1(0.1, 10)

print("5 terms", tay_5)
print("10 terms", tay_10)

#3 c)
original = 1/(1-0.1)
error_5 = original - tay_5
error_10 = original - tay_10
print("Original", original)
print("Error 5 ", error_5)
print("Error 10", error_10)
