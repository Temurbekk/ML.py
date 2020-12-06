from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

# print the output of the training
print(predictions)

# test the accuracy
print(accuracy_score(y_test, predictions))
