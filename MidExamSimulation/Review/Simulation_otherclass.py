import numpy as np
import matplotlib.pyplot as plt
import math

# Simulation other class
# Mid Exam Simulation.docx
# ----------------------------
# 1
a = np.array([12.5, 11.4, 15.7,
              13.1, 12.9, 14.1,
              ])

# a)
mean = np.mean(a)
std = np.std(a, ddof=1)
n = len(a)
print("Mean ", mean)
print("Standard Deviation ", std)

# b)
Q = np.percentile(a, [25, 50, 75])
print("Percentile ", Q)

# c)
fig = plt.figure();
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.ones(n), a, 'o')
ax.errorbar(1.2, mean, std, capsize=5)
ax.plot(1.2, mean, 'sk')
ax.boxplot(a, positions=[0.8])
ax.set_xlim([0, 2])
ax.set_ylim([10, 17])
ax.set_title("Problem 1")
fig.tight_layout()
# plt.show()

# -----------------------------
# 2
print('========= PROBLEM 2 ==========')


def mycos(x, n):
    total = 0
    for i in range(n):
        # total = total + (-1)**i * (8*x)**(2*i) / fact(2*i)
        total = total + (-1) ** i * (x) ** (2 * i) / math.factorial(2 * i)
    return total


x = 3 / 8 * np.pi
n = 20

value = mycos(x, n)
realValue = np.cos(8 * x)
print("mycos ", value)
print("numpy cos ", realValue)

# ----------------------------
# 3
A = np.array([
    [3, 1, 0, 0],
    [2, 3, 2, 0],
    [1, 2, 4, 1],
    [0, 1, 1, 2]
])

b = np.array([
    [1],
    [1],
    [1],
    [1]
])

x = np.linalg.solve(A, b)
print(x)

# b)
det_A = np.linalg.det(A)
print("determinant A", det_A)

norm_b = np.linalg.norm(b)
print("||b2|| ", norm_b)