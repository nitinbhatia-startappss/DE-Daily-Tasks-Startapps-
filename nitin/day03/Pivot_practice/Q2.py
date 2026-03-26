'''
Q1. Create this DataFrame and make a pivot table showing Average by Region and Product:
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
  index ='Region',
  columns = 'Product',
  aggfunc = 'mean'
)

print(pivot)