# Collection of snippen for charting

## Plotly Express

### Simple bar chart time series
```
def bar_chart_timeseries(df, indicator, x_labels):
  fig = px.bar(df[[x_labels, indicator]],
              x = x_labels,
              y = indicator,
              text = df[indicator]/1000000)
  fig.update_layout(title = dict(text = indicator),
                    #xaxis = {'title': 'Report Date', 'tickmode': 'linear'},
                    xaxis = dict(title = x_labels, tickmode = 'array')
                    )
  fig.update_traces(
      texttemplate='%{text:,}',   # format (e.g., 2 significant digits)
      textposition='outside'        # position labels outside the bars
  )
  fig.show()
```
Use:
```
indicator = 'Revenue'
x_labels = 'Report Date'
bar_chart_timeseries(apple_df, indicator,x_labels)
```
<img width="1656" height="612" alt="image" src="https://github.com/user-attachments/assets/8db63216-e90e-4497-ac04-fd649b093b67" />


### Distribution histogram

**Basic**
```
fig = px.histogram(apple_df['% Change in Quarterly EPS (Target Output)'] * 100, nbins = 30)
fig.update_layout({'plot_bgcolor': "white"})
```
<img width="1704" height="618" alt="image" src="https://github.com/user-attachments/assets/ddf14917-bfc1-4e07-bb72-2dde75aea76e" />

**Styled**
```

fig = px.histogram(
    apple_df['% Change in Quarterly EPS (Target Output)'] * 100,
    nbins=30,
    opacity=0.75,               # slight transparency
#    marginal="box",             # optional: add a boxplot on top
    color_discrete_sequence=["#1f77b4"]  # custom color
)

fig.update_layout(
    title="<b>Distribution of Quarterly EPS % Change (Target Output)</b>",
    title_x=0.5,   # center the title
    plot_bgcolor="white",
    paper_bgcolor="white",
    xaxis=dict(
        title="Quarterly EPS Change (%)",
        gridcolor="lightgray",
        zeroline=False
    ),
    yaxis=dict(
        title="Count",
        gridcolor="lightgray",
        zeroline=False
    ),
    bargap=0.05,   # space between bars
)
```

<img width="1688" height="625" alt="image" src="https://github.com/user-attachments/assets/4589989f-be02-48e5-95ad-57f9bca1ec57" />

## Matrix

```
# Let's use Seaborn to display a heatmap for the correlation matrix
f, ax = plt.subplots(figsize = (15, 9))
sns.heatmap(correlation_matrix, annot = True);
```

