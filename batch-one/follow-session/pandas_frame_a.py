#!/usr/bin/python3
import pandas as pd
raw_data = {
             'subject_id': ['1', '2', '3', '4', '5'],
             'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
             'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
          }

df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

print (df_a)

