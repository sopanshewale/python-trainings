#!/usr/bin/python3
import pandas as pd

raw_data = {
             'one': [10, 23, 45, 12, 34],
             'two': [23, 23, 45, 67, 12]
           }

df = pd.DataFrame(raw_data)
print (df)

df['sum'] = df[['one', 'two']].sum(axis=1)
print (df)

df['max'] = df[['one', 'two']].max(axis=1)
print (df)

df['min'] = df[['one', 'two']].min(axis=1)
print (df)


####  apply and lambda way 

df['lambda_sum'] = df.apply(lambda row: row['one'] + row['two'], axis=1)
print (df)








