## ausführbares Dashboard für den Prototyp 
# Das ist die allgemeine Oberfläche und alles unter dem Ordner Pages sind die Unterseiten zu dem Dashboard

from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
	html.H1('Gendergerechte Sprache in Songtexten'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)