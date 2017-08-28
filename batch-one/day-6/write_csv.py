#!/usr/bin/python3
import pandas as pd
data ={
      'year': ['2002','2003','2004','2005'],
      'speed': ['9.0','10.0','9.5', '8.9'],
      }
df = pd.DataFrame(data)
print (df)

df.to_csv('myspeed.csv', sep='|', index_label='Number')
#df.to_csv('myspeed.csv', sep='|', index=False)


