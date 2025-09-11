# Code for data preparation

## Display options

```
pd.options.display.max_columns = 70
pd.options.display.max_rows = 70
pd.options.display.float_format = '{:,.3f}'.format
```

## Dealing with null values

### ```dropna``` by subest 
```
apple_df.dropna(subset = ['Next Quarter EPS']).reset_index(drop = True)
```

### dropna for all nulls
```
apple_df.dropna().reset_index(drop = True)
```


## Feature Engineering

### Lambda function 
def create_regression_label(next_quarter, current_quarter):

    # If the current quarter EPS value is zero, we set the label to zero
    # Calculating the % change would result in an infinite number
    if abs(current_quarter) == 0:
        return 0
    return (next_quarter - current_quarter) / abs(current_quarter)

apple_df['% Quarterly Change in EPS (Regression Label)'] =\
apple_df.apply(lambda row: create_regression_label(row['Next Quarter EPS'], row['Earnings Per Share, Basic']), axis = 1)

apple_df


### ```.pct_change()```
e.g. % change of assets
```
apple_df['Total Assets change from last quarter'] = apple_df['Total Assets'].pct_change()
```


## Statistics
### Correlation matrix
```
correlation_matrix = apple_df.corr()

# restrict to numeric columns
correlation_matrix = apple_df.select_dtypes(include=['number']).corr() 
```
