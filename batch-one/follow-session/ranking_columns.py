#!/usr/bin/python3
import pandas as pd

data = {
        'Mathematics': [100, 64, 56, 70, 85],
        'Science': [25, 94, 57, 62, 70]
      }
name =  ['Kiran', 'Anup', 'Tina', 'Mallika', 'Bharati']
df = pd.DataFrame(data, index = name)
print (df)

df['Total'] = df.apply(lambda row: row['Mathematics'] + row['Science'], axis=1)
print (df)


#df['Rank'] = df['Total'].rank(ascending=1)
df['Rank'] = df['Total'].rank(ascending=0, method='max').astype(int)

print (df)


