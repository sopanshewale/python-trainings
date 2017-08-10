#!/usr/bin/python3
import pandas as pd
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [1, 2, 1, 2, 3],
        'coverage': [2, 2, 3, 3, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print (df)

# Sort the dataframe's rows by reports, in descending order
 
x = df.sort_values(by='reports', ascending=0)

print (x)

# Sort the dataframe's rows by coverage and then by reports, in ascending order

y = df.sort_values(by=['coverage', 'reports'])

print (y)

