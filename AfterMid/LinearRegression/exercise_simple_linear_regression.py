import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([38,50,15,30,50,38,50,20,45,50,20,35,30,43,35,37.5,37,35,30,45,4,37.5,25,46,30,200,200,30]).reshape((-1,1))
y = np.array([8000,6400,2500,3000,6000,5000,8000,4000,11000,25000,4000,8800,5000,7000,8000,18000,5400,15000,3500,24000,1000,8000,2100,8000,4000,1000,2000,4800])


model = LinearRegression().fit(x,y)
rsq = model.score(x,y)
print('coefficient of determination : ', rsq)

print("Intercept : ", model.intercept_)
print("Slope : ", model.coef_)

y_pred = model.predict(x)
print("Predicted respones : ", y_pred, sep="\n")


fig = plt.figure(1)
plt.clf()

ax = fig.add_subplot(1,2,1)

ax.scatter(x,y)
plt.title("Original")
plt.xlabel("Hours/week")
plt.ylabel("Income")
ax.plot(x, y_pred)




x = np.array([38,50,15,30,50,38,50,20,45,50,20,35,30,43,35,37.5,37,35,30,45,4,37.5,25,46,30,30]).reshape((-1,1))
y = np.array([8000,6400,2500,3000,6000,5000,8000,4000,11000,25000,4000,8800,5000,7000,8000,18000,5400,15000,3500,24000,1000,8000,2100,8000,4000,4800])

model = LinearRegression().fit(x,y)
rsq = model.score(x,y)
print('coefficient of determination : ', rsq)

print("Intercept : ", model.intercept_)
print("Slope : ", model.coef_)

y_pred = model.predict(x)
print("Predicted respones : ", y_pred, sep="\n")



ax2 = fig.add_subplot(1,2,2)

ax2.scatter(x,y)
plt.title("Without Outlayer")
plt.xlabel("Hours/week")
plt.ylabel("Income")
ax2.plot(x, y_pred)
plt.show()