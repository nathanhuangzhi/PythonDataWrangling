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
# print(data.head())
print(stats.ttest_ind(data[data['city'] == 'large']['Sale'],data[data['city'] == 'medium']['Sale']))