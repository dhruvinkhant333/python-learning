# We will use the simple Iris dataset, which contains sepal and petal
# measurements for three varieties of iris flowers.

from sklearn import datasets

iris = datasets.load_iris()
print(f"Dataset keys: {list(iris.keys())}")
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
test_features = iris.data[-1:]
test_target = iris.target[-1:]
prediction = clf.predict(test_features)
print(f"Predicted label: {prediction[0]}")
print(f"Predicted class: {iris.target_names[prediction[0]]}")
print(f"Actual class: {iris.target_names[test_target[0]]}")
print(f"Correct prediction: {prediction[0] == test_target[0]}")