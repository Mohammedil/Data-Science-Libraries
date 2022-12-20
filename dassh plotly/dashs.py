from dash import Dash
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



# app = Dash(__name__)

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

#--------------------------------------------------------------------------------------------

# app = Dash(__name__)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# fig = px.scatter(df, x="gdp per capita", y="life expectancy",
#                  size="population", color="continent", hover_name="country",
#                  log_x=True, size_max=60)

# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

#-----------------------------------------------------------------------------------
# app = Dash(__name__)

# app.layout = html.Div([
#     html.Div(children=[
#         html.Label('Dropdown'),
#         dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

#         html.Br(),
#         html.Label('Multi-Select Dropdown'),
#         dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
#                      ['Montréal', 'San Francisco'],
#                      multi=True),

#         html.Br(),
#         html.Label('Radio Items'),
#         dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
#     ], style={'padding': 10, 'flex': 1}),

#     html.Div(children=[
#         html.Label('Checkboxes'),
#         dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
#                       ['Montréal', 'San Francisco']
#         ),

#         html.Br(),
#         html.Label('Text Input'),
#         dcc.Input(value='MTL', type='text'),

#         html.Br(),
#         html.Label('Slider'),
#         dcc.Slider(
#             min=0,
#             max=9,
#             marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
#             value=5,
#         ),
#     ], style={'padding': 10, 'flex': 1})
# ], style={'display': 'flex', 'flex-direction': 'row'})

#-------------------------------------------------------


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H1('US Agriculture Exports (2011)'),
    html.H3(generate_table(df))
])

if __name__ == '__main__':
    app.run_server(debug=True)

