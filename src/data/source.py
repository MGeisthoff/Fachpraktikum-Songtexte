from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from ..data.loader import DataSchema
from .loader import DataSchema


@dataclass
class DataSource:
    _data: pd.DataFrame

    def filter(
        self,
        ids: Optional[list[int]] = None,
        nouns: Optional[list[str]] = None,
        genders: Optional[list[str]] = None,
        year_min: Optional[list[int]] = None,
        year_max: Optional[list[int]]= None,
        artists: Optional[list[str]] = None,
        popularities: Optional[list[int]] = None,
        
        
        #months: Optional[list[str]] = None,
        #categories: Optional[list[str]] = None,
    ) -> DataSource:
        if year_min is None:
            year_min = self.unique_years.min
        if artists is None:
            artists = self.unique_artists
        if popularities is None:
            popularities = self.unique_popularities
        if genders is None:
            popularities = self.unique_genders
        if nouns is None:
            popularities = self.unique_nouns
        filtered_data = self._data.query(
            "year in @years and artists in @artists and popularities in @popularities and genders in @genders and nouns in @nouns"
        )
        return DataSource(filtered_data)

    def create_pivot_table(self) -> pd.DataFrame:
        pt = self._data.pivot_table(
            values=DataSchema.GENDER,
            index=[DataSchema.YEAR, DataSchema.POPULARITY],
            aggfunc="count",
            fill_value=0,
            dropna=False,
        )
        return pt.reset_index().sort_values(DataSchema.GENDER, ascending=False)

    @property
    def row_count(self) -> int:
        return self._data.shape[0]
    
    @property
    def all_ids(self) -> list[str]:
        return self._data[DataSchema.ID].tolist()
    
    @property
    def all_nouns(self) -> list[str]:
        return self._data[DataSchema.NOUN].tolist()
    
    @property
    def all_genders(self) -> list[str]:
        return self._data[DataSchema.GENDER].tolist()

    @property
    def all_years(self) -> list[int]:
        return self._data[DataSchema.YEAR].tolist()

    @property
    def all_artists(self) -> list[str]:
        return self._data[DataSchema.ARTIST].tolist()

    @property
    def all_popularities(self) -> list[int]:
        return self._data[DataSchema.POPULARITY].tolist()
    
    @property
    def unique_ids(self) -> list[str]:
        return sorted(set(self.all_ids), key=int)   

    @property
    def unique_nouns(self) -> list[str]:
        return sorted(set(self.all_nouns))
    
    @property
    def unique_genders(self) -> list[str]:
        return sorted(set(self.all_genders))

    @property
    def unique_years(self) -> list[str]:
        print(sorted(set(self.all_years), key=int))
        return sorted(set(self.all_years), key=int)

    @property
    def unique_artists(self) -> list[str]:
        return sorted(set(self.all_artists))
    
    @property
    def unique_popularities(self) -> list[str]:
        return sorted(set(self.all_popularities), key=int)   
