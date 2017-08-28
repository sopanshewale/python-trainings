#!/usr/bin/python3

import pandas as pd
import numpy as np

raw_data = {
            'student_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 
                              'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
            'test_score': [76, 88, 84, 67, 53, 96, 64, 91, 77, 73, 52, np.NaN]}


df = pd.DataFrame(raw_data, columns = ['student_name', 'test_score'])

print (df)


# Create a list to store the data
grades = []

# For each row in the column,
for row in df['test_score']:
    # if more than a value,
    if row > 95:
        grades.append('A')
    elif row > 90:
        grades.append('A-')
    elif row > 85:
        grades.append('B')
    elif row > 80:
        grades.append('B-')
    elif row > 75:
        grades.append('C')
    elif row > 70:
        grades.append('C-')
    elif row > 65:
        grades.append('D')
    elif row > 60:
        grades.append('D-')
    else:
        grades.append('Failed')

# Create a column from the list
df['grades'] = grades


print (df)


