# Code for data preparation


## Dealing with null values

### ```Dropna``` by subest 
apple_df.dropna(subset = ['Next Quarter EPS']).reset_index(drop = True)
