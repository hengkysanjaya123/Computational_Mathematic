import matplotlib.pyplot as plt
import math


h = 0.1 #step size
n = 5 #number of step

arrayY = []
arrayT = []
y0 = 1 #yn in step 0
# y1 = 0 #yn+1
t0 = 0 #

for j in range(0, n):
    # m = 2 * y0
    m  = 2 - math.pow(math.e, -4 * t0) - (2* y0)
    #m = f(tn, yn)

    arrayY.append(y0)
    arrayT.append(t0)

    y1 = y0 + m * h
    #yn+1 = yn + f(tn, yn) * h


    t1 = t0 + h
    #tn = tn-1 + h
    t0 = t1
    y0 = y1

    print(y1)

plt.plot(arrayT, arrayY, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
# plt.plot(arrayT, arrayY , 'o', color='red')

plt.show()
