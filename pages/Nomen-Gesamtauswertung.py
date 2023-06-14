import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table,dcc
from dash.dependencies import Input, Output
import json
import numpy as np


dash.register_page(__name__)
df0 = pd.read_csv("Dash_Nomen.csv", sep=';')


layout = html.Div(
    children=[
    html.H1(children ='Nomen'),
    html.Div(
            children=[
                html.H2("Alle vorkommenden Nomen"),
                html.Div(
                    children=[
                        html.P("Playlist auswählen:"),
                        dcc.Dropdown(
                            id="select_playlist_n",
                            options=[
                                {"label": "Beliebteste Deutsche Songs", "value": "Beliebteste"},
                                {"label": "Songs 90er", "value": "Songs90er"},
                                {"label": "Songs 2022", "value": "Songs22"},
                            ], value="Beliebteste",
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
 
    html.Div(id='output_container_n', children=[]),
    html.Br(),

    dcc.Graph(id='my_nomen_map', figure={})
])
@callback(
    [Output(component_id='output_container_n', component_property='children'),
     Output(component_id='my_nomen_map', component_property='figure')],
    [Input(component_id='select_playlist_n', component_property='value')]
)
def graph_1(option_slctd): #muss identische sein zum Input


    container = "Die ausgewählte Playlist ist: {}".format(option_slctd)

    dff = df0.copy()
    dff = dff[dff["Playlist"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.histogram(
        data_frame=dff,
        x= ['Wort'],
        template='plotly_white',

    )
    
    




    return container, fig #anzahl Output= so viele Variabeln brauchen wird
