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


for name, group in df.groupby('key1'):
    print (name, "--->")
    print (group)

