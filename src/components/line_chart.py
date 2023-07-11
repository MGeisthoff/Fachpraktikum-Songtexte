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
            Input(ids.YEAR_SLIDER_MIN, "value"),
            Input(ids.YEAR_SLIDER_MAX, "value"),
            Input(ids.POPULARITY_SLIDER_MAX, "value"),
            Input(ids.POPULARITY_SLIDER_MIN, "value"),
            #Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_RADIO, "value"),
        ],
    )
    def update_line_chart(
        years: list[str], months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_source = source.filter(years, months, categories)
        if not filtered_source.row_count:
            return html.Div("Keine Daten ausgewählt", id=ids.LINE_CHART)
        
        
        fig = px.line(
            filtered_source.create_pivot_table(),
            x=DataSchema.YEAR,
            y=DataSchema.AMOUNT,
            color="#1E9D8E",
            labels={
                "category": "Kategorie",
                "amount": "Menge",
            },
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
