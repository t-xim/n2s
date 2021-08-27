from sklearn.tree import DecisionTreeRegressor

RANDOM_STATE = 1

model = DecisionTreeRegressor(random_state = RANDOM_STATE)
model.fit(X, y)

predictions = model.predict(X_test)
