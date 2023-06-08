#pip install dash
#pip install pandas
#pip install plotly.express
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
# Import packages
from dash import Dash, html, dash_table
import pandas as pd

from dash import Dash, html

# Incorporate data
df = pd.read_json('Nomen_soritiert.json')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Auswertung von genderneutraler Sprache in Songtexten'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='Geschlecht', y='Anzahl', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    