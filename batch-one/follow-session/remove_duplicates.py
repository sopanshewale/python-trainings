#!/usr/bin/python3
import pandas as pd

raw_data = {'first_name': ['Jason', 'Jason', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Miller', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 42, 36, 24, 73],
        'preTestScore': [4, 4, 31, 2, 3],
        'postTestScore': [25, 25, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print (df)


# duplicate identify 

duplicates = df.duplicated()

print (duplicates)

y  = df.drop_duplicates()
print (y)

z = df.drop_duplicates(keep='last')

print (z)

