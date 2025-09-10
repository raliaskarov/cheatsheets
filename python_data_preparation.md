# Code for data preparation


## Dealing with null values

### ```dropna``` by subest 
```
apple_df.dropna(subset = ['Next Quarter EPS']).reset_index(drop = True)
```

### dropna for all nulls
```
apple_df.dropna().reset_index(drop = True)
```
