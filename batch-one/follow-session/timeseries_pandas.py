import pandas as pd
import numpy as np


df = pd.DataFrame()

df['german_army'] = np.random.randint(low=20000, high=30000, size=100)
df['allied_army'] = np.random.randint(low=20000, high=40000, size=100)
df.index = pd.date_range('1/1/2014', periods=100, freq='H')

print (df.head())

# Truncate the dataframe

trunk_df = df.truncate(before='1/2/2014', after='1/3/2014')
print ("head")
print (trunk_df.head())
print ("tail")
print (trunk_df.tail())

# Set the dataframe's index
df.index = df.index + pd.DateOffset(months=4, days=5)

print (df.head())

# Lead a variable 1 hour

df.shift(1).head()
print (df.head())

# Aggregate into days by summing up the value of each hourly observation

df.resample('D').sum()

