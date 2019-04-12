import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


a = np.array([100, 110, 105, 102, 120, 100, 115, 107, 105, 107, 105])

min = np.amin(a)
print("min",min)

max = np.amax(a)
print("max" , max)

result = np.where(a == min)
print(result)
# listMinIndex = list(zip(result[0], result[1]))
# for i in listMinIndex:
#     print(i)


print("Sample Standard Deviation : ")
print(np.std(a, ddof=1))

print("Q1 : ")
print(np.percentile(a, 25))
print("Q2 : ")
print(np.percentile(a, 50))
print("Q3 : ")
print(np.percentile(a, 75))

# Histogram ----------------------------------------------------
plt.style.use('ggplot')
x = a
xMean, xStd = stats.norm.fit(x)
xp = np.linspace(x.min(), x.max(), len(x))
pdf = stats.norm.pdf(xp, loc=xMean, scale=xStd)
fig = plt.figure(1);plt.clf()
ax = fig.add_subplot(1,1,1)
ax.hist(x, rwidth=0.9, density=True, label='Data')
ax.plot(xp, pdf, label='Estimated')
ax.legend()
fig.tight_layout()
plt.show()


# Blox plot ----------------------------------------------------
n = len(a)

Q = np.percentile(a, [25, 50, 75], interpolation='midpoint')

fig = plt.figure(1)

ax = fig.add_subplot(1, 1,1)

ax.boxplot(a, vert = False)
ax.plot(a, 0.75 * np.ones(n) , 'or')
ax.plot(Q, 1.25 * np.ones(3), 's')
ax.set_ylim([0.5 , 1.5])

# print(np.ones(n) * 2)
# print(np.ones(3))


fig.tight_layout()
plt.show();