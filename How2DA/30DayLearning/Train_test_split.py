from sklearn.model_selection import train_test_split

RANDOM_STATE = 1


X_train, y_train, X_valid, y_valid = train_test_split(X, y, random_state = RANDOM_STATE)
