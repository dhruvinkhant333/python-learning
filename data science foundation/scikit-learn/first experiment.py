# We will use a
# simple dataset called iris dataset that contains the petal and sepal
# length of three varieties of iris lowers 

from sklearn import datasets 
from pprint import pprint

pprint([name for name in dir(datasets) ])

iris = datasets.load_iris()
pprint(iris)
print(iris.keys())

# print irst ive items from the iris dataset, followed by
# their labels, or the targets as follows
print(iris.data[:10])
print(iris.target[:5])

#print columns names that represent the feature names : 
print(iris.feature_names)                                                                   
    
#print targets (iris varienties : ) :
print(iris.target_names)

# As the irst ive elements that we printed have target as 0, they
# belong to the type setosa, which is the smallest lower in the dataset.

# We will now create an estimator with an algorithm called Support Vector Machines (SVM) Classiier that we will study in detail in a dedicated chapter. To initialize and learn the parameters, use the following lines of code

from sklearn import svm

clf = svm.SVC(gamma = 0.001, C=100.)
clf.fit(iris.data[:-1], iris.target[:-1])
print(clf.predict(iris.data))