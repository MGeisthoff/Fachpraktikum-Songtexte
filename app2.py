## ausführbares Dashboard
# Das ist die allgemeine Oberfläche und alles unter dem Ordner Pages sind die Unterseiten zu dem Dashboard

from dash import Dash, html, dcc, Input, Output, callback
import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from src.components import (
    line_chart
)
from src.components.layout import create_layout
from src.data.loader import load_transaction_data
from src.data.source import DataSource

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


#app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SLATE])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
# 	html.H1('Sprachanalyse von Songtexten'),

#     html.Div(
#         [
#             html.Div(
#                 dcc.RangeSlider(1972, 2023, 1, count=1, value=[1990, 2023])
                
#             )
#             for page in dash.page_registry.values()
#         ]
#     ),

# 	dash.page_container
# ])

# if __name__ == '__main__':
# 	app.run_server(debug=True)

DATA_PATH = "./data/Nomen_csv.csv"

data = load_transaction_data(DATA_PATH)
data = DataSource(data)

app.layout = html.Div(
    className="app-div",
    children=[
        html.H1('Sprachanalyse von Songtexten'),
        
        html.Div(className="graph",
                 children=[
                html.H2('Platzhalter'),
           # dcc.Graph()
                line_chart.render(app, data)
                
        ]),   
            
        html.Div(className="navigation",
                 children=[
            html.H3('Eigenschaften'),
            html.Div([
                html.Label('Jahre'),
                dcc.RangeSlider(1970, 2023, 1, marks=None, value=[1990, 2023], id='year-slider', tooltip={"placement": "bottom", "always_visible": True})]),
                #html.Div(id='output-container-year-slider'),
            html.Div([
                html.Label('Popularität'),
                dcc.RangeSlider(0, 100, 1, marks=None, value=[0, 100], id='popularity-slider', tooltip={"placement": "bottom", "always_visible": True})]),
                html.Div(id='output-container-popularity-slider'),
        ])
    ])
    

@callback(
    [
        Output('line-chart', 'figure')
       # Output('output-container-year-slider', 'children'),
       # Output('output-container-populartity-slider', 'children'),
    ],
    [
        Input('year-slider', 'value'),
        #Input('popularity-slider', 'value'),
              
    ]
                                    
                                    
 )
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()