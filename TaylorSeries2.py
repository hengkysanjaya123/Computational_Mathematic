import numpy as np
import matplotlib.pyplot as plt
import math

x = 0.5
a = 0.1
actual_value = np.exp(x)


sum = 0;
for i in range(0,11):
    sum += (np.exp(a) / math.factorial(i)) * (x - a)**i

print("Actual Value ", actual_value)
print("Approx Value ", sum)

deviation = abs(actual_value - sum)
dev_ratio = deviation / sum
print("Deviation ", deviation)
print("Dev Ratio , ", dev_ratio)

