#Q4. Using that Region_Total column, calculate what percentage each product contributes to its region's total
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
df['percentage'] = (df['Sales']/ df['Region_total'])*100
print(df)