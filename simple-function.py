import pandas as pd 
import numpy as np 


df = pd.read_excel('~/Downloads/excel-to-pandas/sample-sales.xlsx')

#1. convert type of column date to datetime
df['date'] = pd.to_datetime(df['date'])

#2. filter by specific value
df[df['account number'] == 218895].head()

#3. filter by number
df[df['quantity'] > 20].head()

#4. use map to more complex filtering
df[df['sku'].map(lambda x: x.startswith('B1'))].head()

#5. filter on various criteria as well
df[df['sku'].map(lambda x: x.startswith('B1')) & (df['unit price'] > 50)].head()

#6. get field is in a list
df[df['account number'].isin([737550, 714466])].head()

#7. select subset of data with a condition
df.query('name == ["Trantow-Barrows", "Kulas Inc"]').head()

#8. sort date
df = df.sort_values(by='date')

#9. filter date
df[df['date'] >= '20140505'].head()

#10. get value more than a specific month
df[df['date'] >= '2013-05'].head()

#11. between condition
df[(df['date'] >= '20140101') & (df['date'] <= '20140331')].head()

#12. pandas knows multiple format of date
df[df['date'] >= 'Oct-2014'].head()

#13. another format
df[df['date'] >= '13-10-2014'].head()

#When working with time series data, if we convert the data to use the date as as the index, we can do some more filtering variations.
#14. set new index 
df_date = df.set_index(['date'])

#15. filter contain string
df[df['sku'].str.contains('B1')].sort_values(by='date')

#16. with multiple condition
df[(df['sku'].str.contains('B1-05')) & (df['quantity'] > 50)].sort_values(by=['quantity', 'name'], ascending=False)

#17. get distinct name
df['name'].unique()

#18. multiple unique columns: account number and name
df.drop_duplicates(subset=['account number', 'name']).head()

#19. select only first and second columns using ix
df.drop_duplicates(subset=['account number', 'name']).ix[:, [0,1]]

print(df.drop_duplicates(subset=['account number', 'name']).ix[:, [0,1]])
