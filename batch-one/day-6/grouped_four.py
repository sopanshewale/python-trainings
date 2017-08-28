#!/usr/bin/python3

import numpy as np
import pandas as pd

df = pd.DataFrame(
        {'Col1'  : ['A', 'B', 'A', 'A', 'B', 'C', 'C', 'C'],
         'Value' : [ 1,   2,   2,   1,   2,   3,   2,    2],
        }
    ) 

print ('df')
print(df)
print ("-----")
df2 = df.groupby(['Col1', 'Value'])
print ("df2 = df.groupby(['Col1', 'Value'])")
print (df2)

print ('df2.size()')
print (df2.size())

print ("-----")

df3 = df2.size().reset_index()
print ('df3 = df2.size().reset_index()')
print ('df3')
print (df3)
print ("-----")
df3.colums = ['Col1', 'Value', 'Count']

print(df3)

