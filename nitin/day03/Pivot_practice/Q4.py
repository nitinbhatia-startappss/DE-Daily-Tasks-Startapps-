'''
Q4. From the Q1 DataFrame, make a pivot table showing sum, mean and count all at once using multiple aggfunc
Region   Product   Sales
North    Laptop    500
North    Phone     300
South    Laptop    400
South    Phone     600
East     Laptop    300
East     Phone     200
'''

import pandas as pd

df = pd.DataFrame({
  'Region' : ['North','North','South','South','East','East'],
  'Product' : ['Laptop','Phone','Laptop','Phone','Laptop','Phone'],
  'Sales': [500,300,400,600,300,200]
})

pivot = df.pivot_table(
  values = 'Sales',
  index = 'Region',
  aggfunc = ['sum','mean','count']
  )
print(pivot)  