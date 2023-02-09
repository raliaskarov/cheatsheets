# Quick hand functions for pandas

## Move selected row to the top of the table

```python
# create sample dataframe
df = pd.DataFrame({'Country': ['Algeria', 'UK', 'Total', 'Canada'],
                  'Wins': [5, 4, 12, 3]})
df.set_index('Country', inplace = True)
df

# move "Total" row to the top
index = list(df.index)
index.remove('Total')
index.insert(0, 'Total')
df = df.reindex(index)
df
```
