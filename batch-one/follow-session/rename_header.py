#!/usr/bin/python3
import pandas as pd
raw_data = {'0': ['first_name', 'Molly', 'Tina', 'Jake', 'Amy'],
        '1': ['last_name', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        '2': ['age', 52, 36, 24, 73],
        '3': ['preTestScore', 24, 31, 2, 3]
       }

df = pd.DataFrame(raw_data)
print (df)

header = df.iloc[0]
print (header)

df = df[1:]

print (df)

#new_df = df.rename(columns = header)
#print (new_df)
df.columns = header
print (df)


