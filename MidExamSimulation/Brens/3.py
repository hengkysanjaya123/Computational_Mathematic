import numpy as np
import math as m

def ln1_x(x, n):
    totalValue = 0
    intN = int(n)
    for i in range(intN):
        value = pow(-x, i + 1) / (i + 1)
        totalValue += value
    return totalValue




def usingLog(x):
    logs = m.log((1-x))
    return logs


#main
# x = float(input("Enter your X value: "))
# n = float(input("Enter your n value: "))
print(ln1_x(0.5,8))
print(ln1_x(0.5,16))

print("using log: ", usingLog(0.5) )

print("diff1: ",usingLog(0.5)-ln1_x(0.5,8))
print("diff1: ",usingLog(0.5)-ln1_x(0.5,16))