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

print ('printing df')
print (df)

# View a column of the dataframe
print ('# View a column of the dataframe - df["name"]')
print (df['name'])

# View two columns of the dataframe
print ("# View two columns of the dataframe df[['name', 'reports']] ")
print (df[['name', 'reports']])

#View the first two rows of the dataframe
print ("#View the first two rows of the dataframe - df[:2]")
print (df[:2])

# View all rows where coverage is more than 50
print ("# View all rows where coverage is more than 50 - df[df['coverage'] > 50]")
print (df[df['coverage'] > 50])

# View a row
print ("# View a row - df.ix['Maricopa']")
print (df.ix['Maricopa'])

#View a column
print ("#View a column  - df.ix[:, 'coverage']")
print (df.ix[:, 'coverage'])

#View the value based on a row and column
print ("#View the value based on a row and column - df.ix['Yuma', 'coverage']")

print (df.ix['Yuma', 'coverage'])

