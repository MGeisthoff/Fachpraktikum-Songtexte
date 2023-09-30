import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        [
            Input(ids.YEAR_SLIDER, "value"),
           # Input(ids.YEAR_SLIDER_MAX, "value"),
            #Input(ids.POPULARITY_SLIDER, "value"),
            #Input(ids.POPULARITY_SLIDER_MIN, "value"),
            #Input(ids.MONTH_DROPDOWN, "value"),
            #Input(ids.CATEGORY_RADIO, "value"),
        ],
    )
    def update_line_chart(
        years_min: list[int], years_max: list[int]  #, months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_source = source.filter(years)#, months, categories)
        if not filtered_source.row_count:
            return html.Div("Keine Daten ausgewählt", id=ids.LINE_CHART)
        
        
        fig = px.line(
            filtered_source.create_pivot_table(),
            x=DataSchema.YEAR,
            y=DataSchema.NOUN,
            color="#1E9D8E",
            labels={
                "years": "Jahre",
                "gender": "Gender",
            },
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)
