#2. Create a pivot table to summarize sales data by region and product category.
import pandas as pd

df = pd.DataFrame({
    'Region': ['North', 'North', 'South', 'South'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
})
pivot = df.pivot_table(
    values ='Sales',
    index = 'Region',
    columns= 'Product',
    aggfunc='sum'
)
print(pivot)
