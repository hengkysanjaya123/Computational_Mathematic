import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

model = LinearRegression()
model.fit(x,y)

rsq = model.score(x,y)
print('coefficient of determination :', rsq)

#b0
print('intercept:', model.intercept_)
#b1
print('slope:',model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')