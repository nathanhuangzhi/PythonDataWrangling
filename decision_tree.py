from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv('F:\ML_Udemy\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 8 - Decision Tree Regression\Python\Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)
print(regressor.predict([[6.5]]))


print(X)

print(max(None,5,None))