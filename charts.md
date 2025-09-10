# Collection of snippen for charting

## Plotly Express

### Simple bar chart time series
```
indicator = 'Revenue'
fig = px.bar(apple_df[['Report Date', 'Revenue']],
             x = 'Report Date',
             y = indicator,
             text = apple_df[indicator]/1000000)
fig.update_layout(title = dict(text = indicator),
                  #xaxis = {'title': 'Report Date', 'tickmode': 'linear'},
                  xaxis = dict(title = 'Report Date', tickmode = 'array')
                  )
fig.update_traces(
    texttemplate='%{text:,}',   # format (e.g., 2 significant digits)
    textposition='outside'        # position labels outside the bars
)
fig.show()
```
<img width="1656" height="612" alt="image" src="https://github.com/user-attachments/assets/8db63216-e90e-4497-ac04-fd649b093b67" />
