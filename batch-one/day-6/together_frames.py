#!/usr/bin/python3
import pandas as pd

raw_a_data = {
             'subject_id': ['1', '2', '3', '4', '5'],
             'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
             'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
          }

df_a = pd.DataFrame(raw_a_data, columns = ['subject_id', 'first_name', 'last_name'])

print ('df_a:  ')
print (df_a)
'''
df_a:  
  subject_id first_name last_name
0          1       Alex  Anderson
1          2        Amy  Ackerman
2          3      Allen       Ali
3          4      Alice      Aoni
4          5     Ayoung   Atiches

'''


raw_b_data = {
              'subject_id': ['4', '5', '6', '7', '8'],
              'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
              'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
           }
df_b = pd.DataFrame(raw_b_data, columns = ['subject_id', 'first_name', 'last_name'])

print ('df_b: ')
print (df_b)
'''
df_b: 
  subject_id first_name last_name
0          4      Billy    Bonder
1          5      Brian     Black
2          6       Bran   Balwner
3          7      Bryce     Brice
4          8      Betty    Btisan
'''


raw_n_data = {
             'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
             'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
           }
df_n = pd.DataFrame(raw_n_data, columns = ['subject_id','test_id'])

print ('df_n:  ')
print (df_n)

'''
df_n:  
  subject_id  test_id
0          1       51
1          2       15
2          3       15
3          4       61
4          5       16
5          7       14
6          8       15
7          9        1
8         10       61
9         11       16
'''

# Join the two dataframes along rows
# by default - axis is 0
#df_new = pd.concat([df_a, df_b])
df_new = pd.concat([df_a, df_b], axis=0)

print ('df_new: ')
print (df_new) 

'''
df_new: 
  subject_id first_name last_name
0          1       Alex  Anderson
1          2        Amy  Ackerman
2          3      Allen       Ali
3          4      Alice      Aoni
4          5     Ayoung   Atiches
0          4      Billy    Bonder
1          5      Brian     Black
2          6       Bran   Balwner
3          7      Bryce     Brice
4          8      Betty    Btisan

'''

# Join the two dataframes along columns

df_new_cols  = pd.concat([df_a, df_b], axis=1)
print ('df_new_cols:')
print (df_new_cols)
'''
df_new_cols:
  subject_id first_name last_name subject_id first_name last_name
0          1       Alex  Anderson          4      Billy    Bonder
1          2        Amy  Ackerman          5      Brian     Black
2          3      Allen       Ali          6       Bran   Balwner
3          4      Alice      Aoni          7      Bryce     Brice
4          5     Ayoung   Atiches          8      Betty    Btisan
'''

# Merge two dataframes along the subject_id value

df_merge = pd.merge(df_new, df_n, on='subject_id')
print ('df_merge: ')
print (df_merge)

#Merge two dataframes with both the left and right dataframes using the subject_id key
print (pd.merge(df_new, df_n, left_on='subject_id', right_on='subject_id'))

# Merge with outer join
print (pd.merge(df_a, df_b, on='subject_id', how='outer'))

# Merge with inner join

print (pd.merge(df_a, df_b, on='subject_id', how='inner'))

# Merge with right join 
print (pd.merge(df_a, df_b, on='subject_id', how='right'))

# Merge with left join

print (pd.merge(df_a, df_b, on='subject_id', how='left'))

# Merge while adding a suffix to duplicate column names
print (pd.merge(df_a, df_b, on='subject_id', how='left', suffixes=('_left', '_right')))

# Merge based on indexes

print (pd.merge(df_a, df_b, right_index=True, left_index=True))



