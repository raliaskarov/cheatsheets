# About

Reminder how to work with classes.
Here we have single function to profile data wrapped in data_exploration class.

# Guide
1. Structure code as follows:
```
# technical function to profile table
class data_exploration:
    def __init__(self, df):
        self.df = df
        
    def profile(self):

        value_types = [[c, df[c].apply(lambda x: type(x)).unique().tolist()] for c in df.columns]

        print('DATAFRAME:')
        print(f'{format(df.shape[0],",d")} rows | {df.shape[1]} columns')
        print(f'{format(df.size,",d")} datapoints')
        print(f'{format(df.memory_usage(deep = False).sum()/1000000,".1f")}MB disk space')

        print('------------------------')

        print('DTYPES:')
        print(df.dtypes)

        print('------------------------')

        print('VALUE TYPES:')
        for v in value_types:
            print(f'{v[0]}: {v[1]}')

        print('------------------------')
        print('COLUMNS:')
        print(df.columns.tolist())
```

2. To use your class:
```
# import packs
import pandas as pd 
import numpy as np

# build random df
data = {'col 1': np.random.rand(10),
           'col 2': np.random.randint(0, 10, 10),
           'col 3': np.random.choice(['A', 'B', 'C'], 10)}
df = pd.DataFrame(data)

# initialise class
data_explorer = data_exploration(df)

# call profile function
data_explorer.profile()
```
