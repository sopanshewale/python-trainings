#!/usr/bin/python3
import pandas as pd
import datetime as dt
import numpy as np


df = pd.Series(['05/23/2005', '05/24/2005'])
print (df)

df = pd.to_datetime(df)
print (df)



# float to int

df = pd.DataFrame(np.random.rand(5, 5) * 5)
print (df)
slc = np.r_[0:4]
print (slc)

# just one column
df[2] = df[2].astype(int)

print (df)


df = df.astype({c: int for c in slc})

print (df)

