import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html

plt.style.use('ggplot')

#
# x= np.linspace(0, 4*np.pi, 1000)
# y = np.sinc(x)
#
# fig = plt.figure(1)
# plt.clf()
#
# ax = fig.add_subplot(1,1,1)
# ax.plot(x,y)

# x = np.array([3450, 4550, 4650, 3480, 3355, 3310, 3490, 3730, 3925, 3520, 3480])
x = np.array([
    5.5, 1.1, 6.5, 4.9, 6.4,
    7.0, 1.5, 5.7, 5.9, 5.4,
    6.1, 1.2, 7.3, 6.1, 4.4,
])
mean = np.mean(x)
std = np.std(x, ddof=1)
n = len(x)
Q = np.percentile(x, [25, 50, 75])

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
# ax.boxplot(x, vert=False, patch_artist=True)
# ax.plot(x, 0.75 * np.ones(n) , 'or')
# ax.plot(Q, 1.25 * np.ones(3), 's')

for i in x:
    plt.plot(1, i, 'or')

# plt.errorbar(2, mean, std,marker='s',capsize=5,color='m')
plt.errorbar(2, mean, std, capsize=5, color='b')
plt.plot(2, mean, 's', color='k')

up = mean + std
down = mean - std

ax.text(2.05, up, 'ẍ+s = ' + str(round(up, 2)), fontsize=8)
ax.text(2.05, mean, 'ẍ = ' + str(round(mean, 2)), fontsize=8)
ax.text(2.05, down, 'ẍ-s = ' + str(round(down, 2)), fontsize=8)

plt.boxplot([[], [], x])

ax.text(3.2, Q[0], 'Q1 = ' + str(Q[0]), fontsize=8)
ax.text(3.2, Q[1], 'Q2 = ' + str(Q[1]), fontsize=8)
ax.text(3.2, Q[2], 'Q3 = ' + str(Q[2]), fontsize=8)

plt.xticks([1, 2, 3], ["Data", "Error Bar", "Boxplot"])

plt.tight_layout()
plt.show()
