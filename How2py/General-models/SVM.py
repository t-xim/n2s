# Assuming X_train and y_train already input.
# Assuming X_test and y_train already input.

from sklearn import svm

# rbf kernel and C = 100
model = svm.SVC(kernel = "rbf", C = 100.0, random_state = 322)
model.fit(X_train, y_train)

# Accuracy
model.score(X_train, y_train)

# Predicting (Not sure if looping in necessary, taken from image processing)
predictions = []

for i in range(len(X_test)):
  to_predict = X_test[i]
  prediction = model.predict(to_predict)
  predictions.append(prediction);

# Accuracy
metric.accuracy_score(y_test, predictions)
