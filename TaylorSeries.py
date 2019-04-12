import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
x = np.linspace(0, 4*np.pi, 1000)
y = np.sin(x)
fig = plt.figure(1)
plt.clf()

ax1 = fig.add_subplot(1,1,1);
ax1.plot(x,y);
ax1.set_xlabel('$x$');
ax1.set_ylabel('$f(x)$')
ax1.text(6,0.6, '$f(x) = sin(x)$')
fig.tight_layout()

plt.show()
print('\n\n\n')
z = 0.25 * np.pi
print('sin(pi/4)', np.sin(z))