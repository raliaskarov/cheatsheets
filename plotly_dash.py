# Cheatsheet for dash

# Table with widebar 
```
app.layout = html.Div([
    html.Div(children='Hello World!'),
    html.Hr(),
    html.Div([
        html.H2('Filters'),
        # filter1 
        dcc.Dropdown(id='filter1',
                        options=[{'label': i, 'value': i} for i in sorted(df['segment'].unique())],
                        placeholder='Segment',
                        multi=True,),
    ], style={'width': '10%', 'float': 'left' ,'display': 'inline-block'}),

    # data table
    html.Div([
        dash_table.DataTable(id='data-table',
                            columns=columns,
                            page_size=100,
                            style_table={
                                'width': '100%',
                                'minWidth': '100%',
                                'height': 650,
                                'minHeight': 650
                                },
                            fixed_rows = { 'headers': True},
                            style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        },
                            style_cell={
                                        'minWidth': '10px',  # Minimum width of each cell
                                        'width': '20px',  # Default width of each cell
                                        'maxWidth': '200px',  # Maximum width of each cell
                                        'overflow': 'hidden',
                                        'textOverflow': 'ellipsis',
                                    },
                            style_cell_conditional=[
                                        {
                                            'if': {'column_type': 'text'},
                                            'textAlign': 'left'
                                        }
                                        ],
                            filter_action='none',
                            sort_action='native',
                            sort_by=[{'column_id': '2024', 'direction': 'desc'}],

                            ),
    ], style={'width': '90%', 'float': 'right', 'display': 'inline-block'}),

])
```
