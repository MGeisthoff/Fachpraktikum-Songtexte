import datetime as dt
from functools import partial, reduce
from typing import Callable

import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


class DataSchema:
    ID = "id"
    NOUN = "noun"
    GENDER = "gender"
    YEAR = "year"
    ARTIST = "artist"
    POPULARITY = "popularity"


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.ID: int,
            DataSchema.NOUN: str,
            DataSchema.YEAR: int,
            DataSchema.ARTIST: str,
            DataSchema.POPULARITY: int,
        },
        encoding='cp1252',
    )
    # preprocessor = compose(
    #     #create_year_column,
    #     #create_month_column,
    # )
    return data #preprocessor(data)
