import pandas as pd

# Given dataframe df

drop_list = ["col1", "col2", "col3"]

df = df.drop(drop_list, axis=1) 
# OR
df.drop(drop_list, axis=1, inplace=True)
# axis 1 for columns 0 for rows
# More details https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe
