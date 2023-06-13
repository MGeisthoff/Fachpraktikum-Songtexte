import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table,dcc
from dash.dependencies import Input, Output
import json
import numpy as np


# Incorporate data
df0= pd.read_csv ('Dash_Pronomen.csv')


# Initialize the app
app = Dash(__name__)


# App layout
app.layout = html.Div(
    children=[
    html.H1(children ='Genderneutrale Sprache in Songtexten'),
    html.Div(
            children=[
                html.H2("Pronomen"),
                html.Div(
                    children=[
                        html.P("Playlist auswählen:"),
                        dcc.Dropdown(
                            id="Dropdown_P",
                            options=[
                                {"label": "Beliebteste Deutsche Songs", "value": "normal"},
                                {"label": "Songs 90er", "value": "90"},
                                {"label": "Songs 2022", "value": "22"},
                            ],
                            placeholder = "Select",
                        ),
                    ],
                ),
            ],
            style={
                "backgroundColor": "#DDDDDD",
                "maxWidth": "800px",
                "padding": "10px 20px",
            },
        ),
     html.Div(
            children=[
                dash_table.DataTable(
                    id='Pronomen_Table',
                    data=df0.to_dict('records'), page_size=10)
                
            ],
            style={
                "backgroundColor": "#DDDDDD",
                "maxWidth": "800px",
                "marginTop": "10px",
                "padding": "10px 20px",
            },
        ),
])

#@app.callback(
#    Output("Pronomen_Table","children"),
#    [Input("Dropdown_P", "value")],)

#def update_output_div(input_value):
#    return f'Output:{input_value}'



# Run the app
if __name__ == 'main':
    app.run_server(debug=True)