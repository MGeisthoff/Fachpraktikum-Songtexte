import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__)

load_figure_template('SLATE')

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
	html.H1('Sprachanalyse von Songtexten'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    # Die Logik zu den einzelnen Seiten mit den Graphen befinden sich in ./pages
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])


if __name__ == '__main__':
    # Test-Umgebung 
    #app.run_server(debug=True)
    # Produktiv-Umgebung
    app.run_server()