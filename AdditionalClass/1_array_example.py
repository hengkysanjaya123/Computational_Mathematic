import numpy as np

a = np.array([[3,7,5], [8,4,3], [2,4,9]])
print("find min")
print(np.amin(a))
print(np.amin(a, axis= 0))
# axis 0 = by column
print(np.amin(a, axis= 1))
# axis 1 = by row



a = np.array([1,2,3,4, 5, 6])
print(np.average(a))
print("Standard Deviation")
#
print(np.var(a))

#standard deviation population
print(np.std(a))

#standard deviation sample
print(np.std(a, ddof=1))


# percentile
print("Percentile")
a = np.array([[30,40,70], [80, 20, 10], [50,90, 60]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

