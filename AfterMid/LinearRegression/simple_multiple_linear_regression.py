import numpy as np
from sklearn.linear_model import LinearRegression

# test = np.array([5,15,25,35,45,55])
# result = []
# for i in test:
#     result.append([i, i**2])
# print(np.array(result))

x = np.array([
        [5,25],
        [15,225],
        [25,625],
        [35,1225],
        [45,2025],
        [55,3025]
    ])
print(x)
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