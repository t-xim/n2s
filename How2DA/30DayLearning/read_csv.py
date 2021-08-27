import pandas as pd

FILE_NAME = ""

X = pd.read_csv(FILE_NAME + "/train.csv", index_col = 0)
y = pd.read_csv(FILE_NAME + "/test.csv", index_col = 0)
