import numpy as np
import matplotlib.pyplot as plt

a = np.array([3450, 3550, 3650, 3480, 3355, 3310, 3490, 3730, 3540, 3925, 3520, 3480])
n = len(a)

Q = np.percentile(a, [25, 50, 75], interpolation='midpoint')

fig = plt.figure(1)

ax = fig.add_subplot(1, 1,1)

ax.boxplot(a, vert = False)
ax.plot(a, 0.75 * np.ones(n) , 'or')
ax.plot(Q, 1.25 * np.ones(3), 's')
ax.set_ylim([0.5 , 1.5])

print(np.ones(n) * 2)
print(np.ones(3))


fig.tight_layout()
plt.show();