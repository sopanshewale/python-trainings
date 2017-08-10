#!/usr/bin/python3
import pandas as pd

df = pd.DataFrame({'Col1': ['A', 'A', 'A', 'B', 'C'], 'Value': [1, 2, 1, 3, 2]})
print (df)
df2 = df.groupby(['Col1', 'Value']).size()
print (df2)

print ("----")


df2 = df.groupby(['Col1', 'Value']).size().reset_index()
print (df2)
df2.columns = ['Col1', 'Value', 'Count']

print (df2)

