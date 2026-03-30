'''
Q4. Create these two DataFrames and concat them into one:
DataFrame 1              DataFrame 2
Name    Sales            Name    Sales
Alice   500              Carol   400
Bob     300              David   600
Make sure the final index is 0,1,2,3 — not repeating!
'''

import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Alice','Bob'],
    'Sales':[500,300]
})

df2 = pd.DataFrame({
    'Name' : ['Carol','David'],
    'Sales': [400,600]
})

result = pd.concat([df1,df2])
print(result)
#To reset the index
res = pd.concat([df1,df2]).reset_index(drop=True)
print(res)