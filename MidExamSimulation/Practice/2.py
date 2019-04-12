import numpy as np
import matplotlib.pyplot as plt


data = [
        5.5, 1.1, 6.5, 4.9, 6.4,
        7.0, 1.5, 5.7, 5.9, 5.4,
        6.1, 1.2, 7.3, 6.1, 4.4,
        ]

x = [1]*len(data)
print(x)
# x = [1, 10, 50]
# y = [2, 5, 20]
# plt.plot(x, y, 'red')
# plt.plot(x, y, 'bo')
#
# plt.plot(x, y, color='green', marker='o', linestyle='dashed'
#          , linewidth=2,markersize=12)

# plt.plot('xlabel', 'ylabel', data=x)

#https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
# plt.scatter(x, data, alpha=0.8, c='red')

minimum = np.min(data)
maximum = np.max(data)
median = np.median(data)
arrayInfo = [minimum, maximum, median]

ax1 = plt.subplot2grid((1, 1), (0, 0))
for i in range(0,15):
    plt.plot(2, data[i], 'co')


plt.errorbar(3, arrayInfo, marker="^")
plt.boxplot(data, positions=[4])
plt.xticks([1, 2, 3, 4], ["","Data", "Error Bar", "Boxplot"])


ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['right'].set_color('w')
ax1.spines['left'].set_color('w')
ax = plt.gca()
ax.grid(True, color='w', alpha=0.3)
ax1.set_facecolor('lightgrey')

plt.show()