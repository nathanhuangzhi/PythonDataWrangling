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

import seaborn as sns
# sns.relplot(x="date",y ="traffic", hue = 'weekend', data=data3)
# sns.relplot(x = 'date',y = 'traffic', kind = 'line',data = data3)
# sns.catplot(x= 'weekday', kind = 'count',data = data3)
# sns.displot(x ='weekday', data = data3)
# sns.displot(x ='weekday', hue = 'holiday', data = data3)
# sns.displot(data3, x="traffic",hue = 'holiday', kind="kde")
# plt.show()


import sklearn.model_selection as ms
x_train, y_train, x_test, y_test = ms.train_test_split(data3.loc[:,data3.columns != 'traffic'],
                                                       data3['traffic'],test_size = 0.2,random_state=0
                                                       )


