#Q3. From the same DataFrame, add a new column Region_Total using transform that shows the total sales of each region next to every row
'''
Region    Product    Sales
North     Laptop     500
North     Phone      300
South     Laptop     400
South     Phone      600
East      Laptop     200
'''

import pandas as pd

df = pd.DataFrame({
  'Region' : ['North','North','South','South','East'],
  'Product' : ['Laptop','Phone','Laptop','Phone','Laptop'],
  'Sales' : [500,300,400,600,200]
  })

df['Region_total'] = df.groupby('Region')['Sales'].transform('sum')
print(df)
