from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(iris.data, iris.target, random_state=3)
clf = DecisionTreeClassifier(max_depth=5,min_samples_leaf=2).fit(Xtrain,Ytrain)

print(clf.score(Xtrain,Ytrain))
print(clf.score(Xtest,Ytest))