import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__)
load_figure_template('SLATE')

df = None
df2 = None

df2 = pd.read_csv('data/Nomen_csv.csv',sep=';', low_memory=False)
#df2 = pd.read_csv('data/Nomen_ausdruecke.csv',sep=';', low_memory=False)
df = pd.read_csv('data/Nomen_mf.csv',sep=',', low_memory=False)
#df4 = pd.read_csv('data/Nomen_gender.csv',sep=';', low_memory=False)


# print(df.columns) 
# print(df['Year'].min())
# print(df['Year'].max())
# print(df['Popularity'].min())
# print(df['Popularity'].max())


layout = html.Div(
    className="app-div",
    children=[
       # html.H1('Sprachanalyse von Songtexten'),
        html.Div(className="graph",
                children=[
                    dcc.Graph(id='bar-chart3'),
                 ]),
        html.Div(className="navigation",
                 children=[
                    html.Div([
                        html.Br(),
                        html.Label('Jahre',className='my-label'),
                        dcc.RangeSlider(
                            className='my-slider',
                            id='year-slider3',
                            min=df['Year'].min(),
                            max=df['Year'].max(),
                            step=1,
                            value=[df['Year'].min(), df['Year'].max()],
                            marks=None,
                            tooltip={"placement": "bottom", "always_visible": True}
                        ),
                    ]),
                    html.Div([
                        html.Label('Popularität',className='my-label'),
                        dcc.RangeSlider(
                            className='my-slider',
                            id='popularity-slider3',
                            min=df['Popularity'].min(),
                            max=df['Popularity'].max(),
                            step=1,
                            value=[df['Popularity'].min(), df['Popularity'].max()],
                            marks=None,
                            tooltip={"placement": "bottom", "always_visible": True}
                        ),
                    ]),
                    # Filter nach Artist entfernt aufgrund von Zeitmangel
                    # html.Div([
                    #     html.Label('Künstler',className='my-label'),
                    #     dcc.Dropdown(
                    #         id='artists-dropdown',
                    #         value=df['Artist']
                    #     ),
                    # ]),
                    html.Div([
                        
                        dcc.RadioItems(id='radio-button5', options=[
                            {'label': 'Datenbasis', 'value': '1'},
                           # Gender Chart wurde aus Zeitgründen entfernt
                           # {'label': 'Gender', 'value': '2'},
                            {'label': 'Ausdrücke', 'value': '3'},
                            {'label': 'Synonyme', 'value': '4'},
                        ],
                        value='4',
                        className='my-radio'
                        ),
                        html.Div(
                        className="radio-sub",
                        children=[
                        dcc.RadioItems(id='radio-button6', options=[
                            {'label': 'männlich', 'value': '1'},
                            {'label': 'weiblich', 'value': '2'},
                        ],
                        inline=True,
                        value='1',
                        className='my-radio'
                        )
                        ]),
                    ]),
                 ]),
])

# Logik Graphen Aktualisieren basierend auf Filter
@callback(
    Output('bar-chart3', 'figure'),
    [
        Input('year-slider3', 'value'),
        Input('popularity-slider3', 'value'),
        Input('radio-button6', 'value'),
    ]
)
def update_chart(selected_year, selected_popularity, selected_value):
    # Filter der Slider auf dataframe anwenden
    filtered_df = df[(df['Year'] >= selected_year[0]) & (df['Year'] <= selected_year[1]) 
                     & (df['Popularity'] >= selected_popularity[0]) & (df['Popularity'] <= selected_popularity[1])]
    if selected_value == '1':
        filtered_df = filtered_df.query('Maennlich == True')
    else:
        filtered_df = filtered_df.query('Maennlich == False')
    
    # Gesamtanzahl der Nomen im Betrachtungszeitrtaum ermitteln
    filtered_total_year_nouns_df2 = df2[(df2['Year'] >= selected_year[0]) & (df2['Year'] <= selected_year[1]) 
                     & (df2['Popularity'] >= selected_popularity[0]) & (df2['Popularity'] <= selected_popularity[1])]
    grouped_total_year_nouns_df2 = len(filtered_total_year_nouns_df2['Year'])
   
    # Anzahl der Ausdrücke ermitteln und in Relation zu der Gesamtanzahl setzen
    grouped_df=filtered_df.groupby('Year')['ID'].nunique().reset_index()
    grouped_df.columns=['Year','Count']
    grouped_df['Relative'] = grouped_df['Count'] / grouped_total_year_nouns_df2
    
    fig = px.bar(grouped_df, x='Year', y='Relative', title='Synonyme für Männer und Frauen in Songtexten', color_discrete_sequence=['#1E9D8E'])
    # Hintergrund und Linienfarbe anpassen
    fig.update_layout(
        plot_bgcolor='#1C1C1C',
        paper_bgcolor='#1C1C1C',
       # font_color='#1E9D8E'
    )
    #fig.update_traces(base_color='#1E9D8E')
    return fig

# Logik Radio-Button für m/w aktikieren/deaktivieren
@callback(
    Output('radio-button6', 'options'),
    [Input('radio-button5', 'value')]
)
def update_radio_button2(selected_value):
    if selected_value == '4':
        return [
            {'label': 'männlich', 'value': '1'},
            {'label': 'weiblich', 'value': '2'}
        ]
    else:
        return [
            {'label': 'männlich', 'value': '1', 'disabled': True},
            {'label': 'weiblich', 'value': '2', 'disabled': True}
        ]

# # Logik Datenquelle ändern bei Ändern des Radiobuttens
# @callback(
#      Output('bar-chart3', 'figure'),
#     [
#         Input('radio-button6', 'value'),
#         Input('year-slider', 'value'),
#         Input('popularity-slider', 'value'),
#      ]
# )
# def update_df(selected_value,selected_year, selected_popularity):
#     if selected_value == '1':
#         update_chart(selected_year, selected_popularity, selected_value)
   








