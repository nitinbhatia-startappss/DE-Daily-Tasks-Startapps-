'''
Q1. Create these two DataFrames and do an Left join on ID:
Table 1 — Students        Table 2 — Marks
ID   Name                 ID   Marks
1    Rahul                1    85
2    Priya                2    90
3    Amit                 4    78
'''

import pandas as pd

Students = pd.DataFrame({
  'ID' : [1,2,3],
  'Name' : ['Rahul','Priya','Amit']
})

Marks = pd.DataFrame({
  'ID' : [1,2,4],
  'Marks' : [85,90,78]
})

result = pd.merge(Students,Marks,on='ID',how='left')
print(result)


