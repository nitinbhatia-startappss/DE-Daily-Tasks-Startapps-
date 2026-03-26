'''
Q3. Create this DataFrame where some combinations are missing and use fill_value=0 to handle the NaN:
Region   Product   Sales
North    Laptop    500
North    Phone     300
South    Laptop    400
East     Phone     200
'''

import pandas as pd

df = pd.DataFrame({
  'Region':['North','North','South','East'],
  'Product':['Laptop','Phone','Laptop','Phone'],
  'Sales':[500,300,400,200]
})

pivot = df.pivot_table(
  values = 'Sales',
  index = 'Region',
  columns = 'Product',
  aggfunc = 'sum',
  fill_value = 0
  )
print(pivot)  
