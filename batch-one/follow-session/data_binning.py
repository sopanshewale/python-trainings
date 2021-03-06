#!/usr/bin/python3
import pandas as pd
import numpy as np

# Remember: 
# Any NA values will be NA in the result. Out of bounds values will be NA in the resulting Categorical object


np_array = np.array([25, 94, np.nan, 62, 70, np.nan, 94, 57, 62, 70, 62, 70])
raw_data = {
           'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 
                        'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 
                        'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
           'company': ['1st', '1st', '2nd', '2nd', 
                       '1st', '1st', '2nd', '2nd',
                       '1st', '1st', '2nd', '2nd'],
           'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 
                    'Cooze', 'Jacon', 'Ryaner', 'Sone', 
                    'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': np_array
        }
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
print (df)

# Define bins as 0 to 25, 25 to 50, 60 to 75, 75 to 100
bins = [0, 25, 50, 75, 100]

# Create names for the four groups
group_names = ['Low', 'Okay', 'Good', 'Great']

# Cut postTestScore
categories = pd.cut(df['postTestScore'], bins, labels=group_names)

df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)

print (categories)

print (df)

print(pd.value_counts(df['categories']))

