# Load libraries
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('AB_NYC_2019.csv')
print(df.iloc[:5, 1:8])

# Create app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create layout
app.layout = dbc.Container([
   dbc.Row([
       dbc.Col([
           dcc.Markdown('# NYC AirBnB Analysis', style={'textAlign': 'center'}),
       ], width=12)
   ]),

   dbc.Row([
       dbc.Col([
           dcc.Markdown('#### Neighborhood'),
           ng := dcc.Dropdown(options=[{'label': x, 'value': x} for x in df.neighbourhood_group.unique()], value='Brooklyn', style={'width': '100%'}),
       ], width=3),

       dbc.Col([
           dcc.Markdown('#### Minimum Nights'),
           Mn := dcc.Input(type='number', value=3, min=1, max=30, step=1, style={'width': '100%'}),
       ], width=3),

       dbc.Col([
               dcc.Markdown('#### Price Range'),
               price_slider := dcc.RangeSlider( min=df.price.min(), max=df.price.max(), step=500, value=[0, 2500], marks={0: '0', 500: '500 ',1000: '1000', 2500: '2500',
                                                                                                                           5000: '5000', 7500: '7500', 10000: '10000'},
               tooltip = {"placement": "bottom", "always_visible": True}),
       ],  width=6),
   ]),

   dbc.Row([
       dbc.Col([
           gr := dcc.Graph(figure={})
       ], width=12)
   ])
])

# Create callback
@app.callback(
   Output(gr, component_property='figure'),
   Input(Mn, 'value'),
   Input(price_slider, 'value'),
   Input(ng, 'value')
)
def update_graph(min_nights, price_range, ng):
   dff = df[(df.minimum_nights <= min_nights) & (df.price >= price_range[0]) & (df.price <= price_range[1]) & (df.neighbourhood_group == ng)]

   fig = px.scatter_mapbox(data_frame=dff, lat='latitude', lon='longitude',  color='price', height = 600, range_color=[0,1000], zoom=10, color_continuous_scale=px.colors.sequential.Sunset, hover_data= {'latitude': False, 'longitude': False, 'room_type': True, 'minimum_nights': True})
   fig.update_layout(mapbox_style='open-street-map')
   return fig

# Run app
if __name__ == '__main__':
   app.run_server(debug=True)
