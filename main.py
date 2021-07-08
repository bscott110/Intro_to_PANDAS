import pandas as pd
import numpy as np

# create a series using available pandas datatypes
series = pd.Series([0,1,"two",3.0,True, np.nan])

print(series)
print(series.dtypes)

# create a dataframe using first of the month dates as index and
# "0123" respectively as columns. Random number from
# 1 to 10 as data entries. Perhaps, you want a random number for each week

months = pd.date_range(start='1/1/2021', end='12/31/2021', freq='MS')
df = pd.DataFrame(np.random.randint(11,size=(12,4)), index=months,columns=list("0123"))
#print(df)
#print(df.dtypes)
print(df.tail(2))


