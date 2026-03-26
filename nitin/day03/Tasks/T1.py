#1. Given two DataFrames, perform an outer join to combine them.

import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'age': [25, 30, 35]
})

result = pd.merge(df1,df2,on='id',how='outer')
print(result)