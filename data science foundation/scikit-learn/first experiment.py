# We will use the simple Iris dataset, which contains sepal and petal
# measurements for three varieties of iris flowers.

from sklearn import datasets

iris = datasets.load_iris()
print(f"Dataset keys: {iris.keys()}")
print(f"Samples: {iris.data.shape[0]}, features: {iris.data.shape[1]}")

# Print the first ten feature rows and the first five labels.
print(iris.data[:10])
print(iris.target[:5])

# Print the feature and target names.
print(iris.feature_names)
print(iris.target_names)

# The first five examples have target 0, so they belong to the setosa class.

# Create a Support Vector Machine classifier and fit it to the examples.

from sklearn import svm

clf = svm.SVC(gamma = 0.001, C=100.)
clf.fit(iris.data[:-1], iris.target[:-1])
print(clf.predict(iris.data))