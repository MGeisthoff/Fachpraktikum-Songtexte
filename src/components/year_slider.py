import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids




def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
    Output(ids.YEAR_SLIDER, 'children'),
    Input('year-slider', 'value')
    )
    def update_output(value):
        return 'You have selected "{}"'.format(value)