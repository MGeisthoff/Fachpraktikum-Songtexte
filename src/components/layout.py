from dash import Dash, html
from src.components import (
    line_chart,
    year_slider,
    # popolarity_slider,
    # genre_dropdown,
    # category_radio,
    # month_dropdown,
    # pie_chart,
    # year_dropdown,
)

from ..data.source import DataSource


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_slider.render(app, source),
                    #popolarity_slider.render(app, source),
                    #category_radio.render(app, source),
                    #category_dropdown.render(app, source),
                ],
            ),
            line_chart.render(app, source),
            #pie_chart.render(app, source),
        ],
    )
