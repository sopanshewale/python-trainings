#!/usr/bin/python3
import pandas as pd

df = pd.DataFrame()

df['name'] = ['John', 'Steve', 'Sarah']
df['gender'] = ['Male', 'Male', 'Female']
df['age'] = [31, 32, 19]

print (df)


def mean_age_by_group(dataframe, col):
    return dataframe.groupby(col).mean()


def uppercase_column_name(dataframe):
    dataframe.columns = dataframe.columns.str.upper()
    return dataframe


x = df.pipe(mean_age_by_group, col='gender')
print (x)

y = x.pipe(uppercase_column_name)
print ('\n\n')
print (y)

