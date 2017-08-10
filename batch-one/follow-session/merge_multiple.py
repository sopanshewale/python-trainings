#!/usr/bin/python3
import pandas as pd

raw_data = {
             'subject_id': ['1', '2', '3', '4', '5'],
             'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
             'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
          }

df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

print (df_a)


raw_data = {
              'subject_id': ['4', '5', '6', '7', '8'],
              'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
              'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
           }
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
print (df_b)

merged_outer = pd.merge(df_a, df_b, on=('subject_id', 'first_name'), how='outer')
print (merged_outer)




