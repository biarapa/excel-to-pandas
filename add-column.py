import pandas as pd
import numpy as np

df = pd.read_excel('~/Downloads/excel-to-pandas/sample-customers.xlsx')

#1. add column Total to sum months
df["Total"] = df["Jan"] + df["Feb"] + df["Mar"]

#2. sum each months and total
sum_row = df[['Jan', 'Feb', 'Mar', 'Total']].sum()

#3. transpose data & convert Series to a DataFrame
df_sum = pd.DataFrame(data=sum_row).T

#4. reindex is to add missing columns and allow pandas to fill the values
df_sum = df_sum.reindex(columns=df.columns)

#5. add to existing DataFrame
df_final = df.append(df_sum, ignore_index=True)
df_final.tail()
print(df_final)