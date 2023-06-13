import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table,dcc
from dash.dependencies import Input, Output
import json
import numpy as np



app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
df0 = pd.read_csv("Dash_Pronomen.csv", sep=';'),
#df2 = pd.read_csv("Dash_Pronomen_unsortiert.csv", sep=';')
#df1 =pd.read_csv("Dash_Nomen.csv", sep=';')

#df = df.groupby(['ID', 'Playlist', 'Feminine Pronomen', 'Maskuline Pronomen'])
#df.reset_index(inplace=True)
#print(df[:5])

# ------------------------------------------------------------------------------
# App layout
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
                            id="select_playlist_p",
                            options=[
                                {"label": "Beliebteste Deutsche Songs", "value": "Beliebteste"},
                                {"label": "Songs 90er", "value": "Songs90er"},
                                {"label": "Songs 2022", "value": "Songs22"},
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
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_pronomen_map', figure={})
])


    
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_pronomen_map', component_property='figure')],
    [Input(component_id='select_playlist_p', component_property='value')]
)
def graph_1(option_slctd): #muss identische sein zum Input
    print(option_slctd)
    print(type(option_slctd))

    container = "Die ausgewählte Playlist ist: {}".format(option_slctd)

    dff = df0.copy()
    dff = dff[dff["Paylist"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.histogram(
        data_frame=dff,
        x= ['Feminine Pronomen', 'Maskuline Prononem'],
        template='plotly_white',

    )



    return container, fig #anzahl Output= so viele Variabeln brauchen wird




# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components





# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)