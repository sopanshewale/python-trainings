#!/usr/bin/python3
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(10))
print (s)
print (s.sample(n=3))

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
print (df)


# remember  frac is float, percentage :)

print (df.sample(frac=0.5, replace=True))

