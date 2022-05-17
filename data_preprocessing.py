import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.model_selection as ms



dataset = pd.read_csv('F:\ML_Udemy\Machine Learning A-Z (Codes and Datasets)\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Python\Data.csv')
# print(dataset.head())

x_train, x_test,y_train, y_test = ms.train_test_split(dataset.iloc[:,:-1].values,
                                                       dataset.iloc[:,-1].values,test_size = 0.2,random_state=0
                                                       )

print(x_train)