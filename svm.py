import pandas as pd
import sklearn.model_selection as ms
from sklearn.svm import SVR
import matplotlib.pyplot as plt
data = pd.read_csv('F:\ML_Udemy\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 7 - Support Vector Regression (SVR)\Python\Position_Salaries.csv')


# x_train, x_test,y_train, y_test = ms.train_test_split(data.iloc[:,1:-1].values,
#                                                        data.iloc[:,-1].values,test_size = 0.2,random_state=0
#                                                        )
X = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

y = y.reshape(len(y),1)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_Y.fit_transform(y)

regressor = SVR(kernel= 'rbf')
regressor.fit(X,y.ravel())

# print(sc_Y.inverse_transform([regressor.predict(sc_X.transform([[6.5]]))]))

plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(regressor.predict(X).reshape(len(y),1)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()