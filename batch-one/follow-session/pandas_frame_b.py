#!/usr/bin/python3
import pandas as pd

raw_data = {
              'subject_id': ['4', '5', '6', '7', '8'],
              'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
              'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
           }
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

print (df_b)


