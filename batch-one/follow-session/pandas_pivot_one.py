#!/usr/bin/python3
import pandas as pd
import numpy as np

raw = {'A': ['foo','foo','foo','foo','foo', 'bar', 'bar', 'bar', 'bar'], 
       'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
       'C': ['small', 'large', 'large', 'small', 'small', 'large', 'small', 'small', 'large'],
       'D': [1, 2, 2, 3, 3, 4, 5, 6, 7]}

df = pd.DataFrame(raw)
print (df)
table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum, fill_value='0.0')
print (table)


