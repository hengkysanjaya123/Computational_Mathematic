import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use('ggplot')
x = np.random.standard_normal(1000)
xMean, xStd = stats.norm.fit(x)
xp = np.linspace(x.min(), x.max(), 1000)
pdf = stats.norm.pdf(xp, loc=xMean, scale=xStd)
fig = plt.figure(1);plt.clf()
ax = fig.add_subplot(1,1,1)
ax.hist(x, rwidth=0.9, density=True, label='Data')
ax.plot(xp, pdf, label='Estimated')
ax.legend()
fig.tight_layout()
plt.show()