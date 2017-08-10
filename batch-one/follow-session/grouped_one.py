#!/usr/bin/python3

import numpy as np
import pandas as pd

df = pd.DataFrame(
        {'key1' : ['a', 'a', 'b', 'b', 'a'],
        'key2' : ['one', 'two', 'one', 'two', 'one'],
        'data1' : np.random.randn(5),
        'data2' : np.random.randn(5),
        }
    ) 

print(df)
grouped = df['data1'].groupby(df['key1'])
print (grouped)
print ("The mean is: ")
print (grouped.mean())
