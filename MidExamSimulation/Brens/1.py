import pandas as pd
import numpy as np

data = pd.read_csv("Data.csv")

mean = data['Litre'].mean()
std = data["Litre"].std()
median = data['Litre'].median()

q1 = np.percentile(data["Litre"], 25)
q3 = np.percentile(data["Litre"], 75)

print("Mean: ", mean)
print("Standard Deviation: ", std)
print("Median: ", median)
print("Q1: ", q1)
print("Q3: ", q3)