#!/usr/bin/python3

import pandas as pd


raw_data = {
             'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
             'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
           }
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])

print (df_n)

