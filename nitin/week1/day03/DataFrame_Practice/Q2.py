'''''
Q2. Create this DataFrame and do a groupby on Region and find the average sales per region:
Region    Product    Sales
North     Laptop     500
North     Phone      300
South     Laptop     400
South     Phone      600
East      Laptop     200
'''

import pandas as pd

df = pd.DataFrame({
    'Region':['North','North','South','South','East'],
    'Product': ['Laptop','Phone','Laptop','Phone','Laptop'],
    'Sales':[500,300,400,600,200]
})
#Average of sales per region

result = df.groupby('Region')['Sales'].mean()
print(result)