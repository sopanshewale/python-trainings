#!/usr/bin/python3
import pandas as pd

df = pd.DataFrame(
         data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                 'year': [2012, 2012, 2013, 2014, 2014],
                 'reports': [4, 24, 31, 2, 3],
                 'coverage': [25, 94, 57, 62, 70]
                },
        index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma']
              )

print (df)

# View a column of the dataframe
print (df['name'])

# View two columns of the dataframe
print (df[['name', 'reports']])

#View the first two rows of the dataframe
print (df[:2])

# View all rows where coverage is more than 50
print (df[df['coverage'] > 50])

# View a row
print (df.ix['Maricopa'])

#View a column
print (df.ix[:, 'coverage'])

#View the value based on a row and column

print (df.ix['Yuma', 'coverage'])

