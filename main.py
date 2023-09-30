#import i18n
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
import dash_bootstrap_components as dbc

from src.components.layout import create_layout
from src.data.loader import load_transaction_data
from src.data.source import DataSource

#LOCALE = "en"
DATA_PATH = "./data/Nomen_csv.csv"


def main() -> None:
    
    # set the locale and load the translations
    #i18n.set("locale", LOCALE)
    #i18n.load_path.append("locale")

    # load the data and create the data manager
    data = load_transaction_data(DATA_PATH)
    data = DataSource(data)

    app = Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    app.title = "Textanalyse von Songtexten"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
