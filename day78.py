from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

X = np.array([[1], [2], [3], [4], [5]]) #Hours Study
y = np.array([1.5, 3.2, 4.8, 6.3, 8.1]) #CGPA Gain
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print('Error:', mean_squared_error(y_test, y_pred))

print('Prediction for 6:', model.predict([[6]]))
