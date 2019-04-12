import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as fig

# data = pd.read_csv("Data.csv")

data = [
        5.5, 1.1, 6.5, 4.9, 6.4,
        7.0, 1.5, 5.7, 5.9, 5.4,
        6.1, 1.2, 7.3, 6.1, 4.4,
        ]
#
# mean = data['Litre'].mean()
# std = data["Litre"].std()
# median = data['Litre'].median()
mean = np.mean(data)
std = np.std(data, ddof=1)
median = np.median(data)

#
# q1 = np.percentile(data["Litre"], 25)
# q3 = np.percentile(data["Litre"], 75)
#
# print(data["Litre"][1])
# print("Mean: ", mean)
# print("Standard Deviation: ", std)
# print("Median: ", median)
# print("Q1: ", q1)
# print("Q3: ", q3)
#

# fig = plt.figure()
#
# fig.set_facecolor('lightgrey')
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

for i in range(0,15):
    plt.plot(1, data[i], 'co')

y = [[] ,[],data]
my_xticks = ["Data", "Error Bar", "BoxPlot"]


plt.errorbar(2,mean, std, marker='s', ms=5, mew=2, solid_capstyle='projecting', capsize=5, color='black')

plt.boxplot(y)

plt.xticks([1,2,3], my_xticks)

# fig = plt.figure()

ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['right'].set_color('w')
ax1.spines['left'].set_color('w')
ax = plt.gca()
ax.grid(True, color='w', alpha=0.3)
ax1.set_facecolor('lightgrey')


plt.show()