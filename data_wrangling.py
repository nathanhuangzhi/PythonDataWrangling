import numpy as np
import math
import pandas as pd
import os


path = 'F:\MKT745.ChengHe'
os.chdir(path)
data = pd.read_csv('OLS_Ads.csv')

# print(data.head())

# print(data[data['Sale'] > 200].head())

# print(data.sort_values(by = ['Sale']).head())

# print(data[pd.isnull(data['Sale'])])

# data_combine = pd.merge(data,data2, how= 'left', on = 'ID')

# data_rbind =  pd.concat([data, data2])

# data_summarise = data.groupby(['city']).mean()
# print(data_summarise)


data3 = pd.read_csv('DAILY_METRICS.csv')

import datetime
# data3['date'] = pd.to_datetime(data3['date'])
# print(data3['date'] - pd.to_datetime('2016-01-01'))

from scipy import stats

# print(data3.columns)  #  date  traffic  conversion  ...  weekend  holiday  week
# print(data3.head())
# print(stats.ttest_ind(data[data['city'] == 'large']['Sale'],data[data['city'] == 'medium']['Sale']))

# print(data3.head())
import matplotlib.pyplot as plt
# plt.scatter(data3['date'],data3['traffic'], c = data3['weekend'])
# plt.plot(data3['date'],data3['traffic'])
# plt.bar(data3['date'],data3['traffic'])
# plt.hist([data3[data3['weekend']==1]['traffic'], data3[data3['weekend']==0]['traffic']],bins = 100,
#         label = ['weekend','weekday'])
# plt.legend()
# plt.show()


### Data visualization using seaborn

import seaborn as sns
# sns.relplot(x="date",y ="traffic", hue = 'weekend', data=data3)
# sns.relplot(x = 'date',y = 'traffic', kind = 'line',data = data3)
# sns.catplot(x= 'weekday', kind = 'count',data = data3)
# sns.displot(x ='weekday', data = data3)
# sns.displot(x ='weekday', hue = 'holiday', data = data3)
# sns.displot(data3, x="traffic",hue = 'holiday', kind="kde")
# plt.show()

### Split data into training and test set
import sklearn.model_selection as ms
x_train, x_test,y_train, y_test = ms.train_test_split(data3.loc[:,~data3.columns.isin(['traffic','date'])],
                                                       data3['traffic'],test_size = 0.2,random_state=0
                                                       )
# print(x_train.head())
# print(y_train.head())


### Linear & Logistic Regression

from sklearn.linear_model import LinearRegression
regr = LinearRegression().fit(x_train,y_train)
# print(regr.coef_)
print(regr.score(x_test,y_test))
from statsmodels.api import OLS, Logit
# print(OLS(y_train,x_train).fit().summary())

# print(Logit(data3['holiday'], data3[['year','month','weekday']]).fit().summary())


### Ridge Regression

from sklearn.linear_model import Ridge
ridger = Ridge(alpha = 1).fit(x_train,y_train)
print(ridger.coef_)
print(ridger.score(x_train,y_train))
print(ridger.score(x_test,y_test))

### Normalization

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)
ridger_scaled = Ridge(alpha = 1).fit(x_train_scaled,y_train)
print(ridger_scaled.coef_)
print(ridger_scaled.score(x_train_scaled,y_train))
print(ridger_scaled.score(x_test_scaled,y_test))


### LASSO

from sklearn.linear_model import Lasso
Lassor = Lasso(alpha = 1).fit(x_train,y_train)
print(Lassor.coef_)
print(Lassor.score(x_train,y_train))
print(Lassor.score(x_test,y_test))


### Cross validation

from sklearn.model_selection import cross_val_score
Lasso_cv = Lasso(alpha=1)
cv_scores = cross_val_score(Lasso_cv,x_train,y_train)
print('Cross Validation: ',cv_scores)



# Grid search
# param_range0 = np.arange(1,10,1)
# Lasso_mcv = Lasso()
# from sklearn.model_selection import validation_curve
# train_score, test_score = validation_curve(Lasso_mcv,x_train,y_train, param_name='alpha',param_range=param_range0, cv = 3)
# before_pd = {'X':param_range0, 'Y':np.mean(test_score,axis = 1), 'Z': np.mean(train_score,axis= 1)}
# perf = pd.DataFrame(before_pd)
# # print(perf)
# sns.lineplot( x = 'X', y = 'Y', color = 'red', data = perf)
# sns.lineplot( x = 'X', y = 'Z', color = 'blue', data = perf)
# plt.show()