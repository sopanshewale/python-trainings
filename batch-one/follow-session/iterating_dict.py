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


dict_data = dict(list(df.groupby('key1')))
#print(dict_data)

print (dict_data['a'])

