# train data that gets deleted
temp_train = train

# First loop
cur_train = temp_train.sort_values("trajectory_id").drop_duplicates("hash")
X = cur_train
temp_train = temp_train[~temp_train.isin(cur_train)]

X = X.add_suffix('_1')
X = X.rename(columns = {"hash_1" : "hash"})

max_hash_count = max(list(train.groupby("hash").size()))


# Other loops
for col_index in range(max_hash_count - 1):
    cur_train = temp_train.sort_values("trajectory_id").drop_duplicates("hash")
    X = X.merge(cur_train, how = "left", on = "hash", suffixes = ("", "_" + str(col_index + 1)))
    temp_train = temp_train[~temp_train.isin(cur_train)]

print(len(X))
X.head()


## For more grouping related cleaning refer to Titanic or Housing projects
