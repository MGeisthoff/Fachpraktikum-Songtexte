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
                html.H2("Häufigste gegenderte Nomen-Vergleich"),
                html.Div(
                    children=[
                        html.P("Playlist auswählen:"),
                        dcc.Dropdown(
                            id="select_playlist_nga",
                            options=[
                                {'label': x, 'value': x, 'disabled':False}
                                for x in df1['Playlist'].unique()
                         ],
                            
                            value=[],
                            placeholder = "Select",
                            multi=True,
                              
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
    

    dcc.Graph(id='my_pronomen_map_nga', figure={})
])
@callback(
    [Output(component_id='my_pronomen_map_nga', component_property='figure'),
     ],
    [Input(component_id='select_playlist_nga', component_property='value')]
)


def graph_1(option_slctd): #muss identische sein zum Input


    #container = "Die ausgewählte Playlist ist: {}".format(option_slctd)

    dff = df1.copy()
    dff = dff[dff["Playlist"] == option_slctd]
    dff = px.data.medals_wide()
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.bar(
        data_frame=dff,
        x= 'Playlist', y='count', color='Geschlecht',
        template='plotly_white',

    )




    return  fig #anzahl Output= so viele Variabeln brauchen wird

