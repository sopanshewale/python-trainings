#!/usr/bin/python3
import pandas as pd
df = pd.DataFrame({'Col1': ['a', 'a', 'a', 'b', 'c'], 'Value': [1, 2, 1, 3, 2]})
print (df)
print (df.groupby([df[c] for c in df.columns]).size().reset_index().rename(columns={0: 'Count'}))

