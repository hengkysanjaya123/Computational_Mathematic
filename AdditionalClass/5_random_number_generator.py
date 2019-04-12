import numpy as np

#No number duplication
x = np.random.choice(10, 5, replace=False)
print(x)

#allow number duplication
x = np.random.choice(10, 5, replace=True)
print(x)