# Assuming X_train and y_train already input.
# Assuming X_test and y_test already input.

from sklearn.neighbors import KNeighborsCLassifier

# Assuming kN = 10
model = KNeighborsClassifier(n_neighbors = 10)
model.fit(X_train, y_train)

# Accuracy
model.score(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
metric_accuracy_score(y_test, prediction)
