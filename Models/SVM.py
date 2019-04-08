# Assuming X_train and y_train already input.

from sklearn import svm

# rbf kernel and C = 100
model = svm.SVC(kernel = "rbf", C = 100.0, random_state = 322)
model.fit(X_train, y_train)

# Accuracy
format(model.score(X_train, y_train)
