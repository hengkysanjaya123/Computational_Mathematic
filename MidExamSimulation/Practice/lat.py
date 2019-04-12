import matplotlib.pyplot as plt
import numpy as np

data = np.array([12.5, 11.4, 15.7, 13.1, 12.9, 14.1]) # Sample data
mean = data.mean()
std = np.std(data, ddof=1)
q = np.percentile(data, [25, 50, 75])
n = len(data)


fig = plt.figure(1); plt.clf()
ax = fig.add_subplot(1,1,1)
ax.plot(np.ones(n), data ,'o')
ax.errorbar(1.2, mean, std, capsize=5)
ax.plot(1.2, mean, "sk")
ax.boxplot(data, positions=[0.8])
ax.set_xlim([0,2])
ax.set_ylim([10,17])
ax.set_title("Problem 1")
plt.show()