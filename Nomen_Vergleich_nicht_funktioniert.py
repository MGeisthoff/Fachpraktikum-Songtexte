
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table,dcc
from dash.dependencies import Input, Output
import json
import numpy as np


dash.register_page(__name__)
df1 = pd.read_csv("Dash_Nomen_genderneutral_Anzahl_1.csv", sep=';')

layout = html.Div(
    children=[
    html.H1(children ='Nomen'),
    html.Div(
            children=[
                html.H2("Ausgewählte Nomen im Vergleich"),
                html.Div(
                    children=[
                        html.P("Playlist auswählen:"),
                        dcc.Dropdown(
                            id="select_playlist_ngvv",
                            options=[
                                {"label": "Beliebteste Deutsche Songs", "value": "Beliebteste"},
                                {"label": "Songs 90er", "value": "Songs90er"},
                                {"label": "Songs 2022", "value": "Songs22"},
                            ],
                            placeholder = "Select",
                             
                            #multi=True,
                        ),
                         dcc.Dropdown(
                            id="select_playlist_ngvvv",
                            options=[
                                {"label": "Maskulin", "value": "Maskulin"},
                                {"label": "Feminin", "value": "Feminin"},
                                {"label": "Neutral", "value": "Neutral"},
                            ],
                            placeholder = "Select",
                            
                            #multi=True,
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
    
    html.Div(id='output_container_ngvv', children=[]),
    html.Br(),

    dcc.Graph(id='my_pronomen_map_ngvv', figure={})
])
@callback(
    [Output(component_id='output_container_ngvv', component_property='children'),
     Output(component_id='my_pronomen_map_ngvv', component_property='figure')],
    [Input(component_id='select_playlist_ngvv', component_property='value'),
     Input(component_id='select_playlist_ngvvv', component_property='value')]
)

def graph_1(option_slctd,option_slctd_2): #muss identische sein zum Input


    container = "Die ausgewählte Playlist ist: {}".format(option_slctd)

    dff = df1.copy()
    dff = dff[dff["Playlist"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.histogram(
        data_frame=dff,
        x= ['count'],
        template='plotly_white',

    )


    return fig, container#anzahl Output= so viele Variabeln brauchen wird
