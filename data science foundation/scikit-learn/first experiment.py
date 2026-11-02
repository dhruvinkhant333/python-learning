# We will use the simple Iris dataset, which contains sepal and petal
# measurements for three varieties of iris flowers.

from sklearn import datasets
from sklearn import svm 

iris = datasets.load_iris()
# print(iris)
# print(iris.keys())

# print(iris.data[:10])
# print(iris.target[:5])

# print(iris.feature_names)

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(iris.data[:-1], iris.target[:-1])
print(clf.predict(iris.data))