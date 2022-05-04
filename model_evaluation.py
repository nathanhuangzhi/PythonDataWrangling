import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

dataset = load_digits()
x , y = dataset.data, dataset.target

# for class_name, class_count in zip(dataset.target_names, np.bincount(dataset.target)):
#     print(class_name,  class_count)


y_imbalanced = y.copy()
y_imbalanced[y_imbalanced!= 1]=0
print(y[0:30])
print(y_imbalanced[0:30])



from sklearn.svm import SVC

Xtrain, Xtest, Ytrain, Ytest = train_test_split(x,y_imbalanced , random_state=0)

svm = SVC(kernel='rbf', C = 1).fit(Xtrain,Ytrain)
print(svm.score(Xtrain,Ytrain))
print(svm.score(Xtest,Ytest))
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
logit = LogisticRegression().fit(Xtrain,Ytrain)
logit_predict = logit.predict(Xtest)
confusion = confusion_matrix(Ytest, logit_predict)

from sklearn.metrics import classification_report
print(classification_report(Ytest,logit_predict))


from sklearn.model_selection import cross_val_score
logit_new = LogisticRegression()
# print(cross_val_score(logit_new, Xtrain, Ytrain, cv= 5, scoring= 'recall'))


from sklearn.model_selection import GridSearchCV

grid_values = {'C': [-1,0,1]}

grid_logit_auc = GridSearchCV(logit,param_grid=grid_values)
grid_logit_auc.fit(Xtrain,Ytrain)

print(grid_logit_auc.best_params_)
# print(grid_logit_auc.best_score_)