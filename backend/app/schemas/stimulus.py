"""Bounded, text-only evidence tables shared by authoring and learner APIs."""
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

Cell = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=200)]
Row = Annotated[list[Cell], Field(min_length=2, max_length=6)]


class DataTable(BaseModel):
    model_config = ConfigDict(extra='forbid')
    caption: str = Field(min_length=1, max_length=300)
    columns: list[Cell] = Field(min_length=2, max_length=6)
    rows: list[Row] = Field(min_length=1, max_length=30)
    note: str | None = Field(default=None, max_length=1000)

    @model_validator(mode='after')
    def rectangular(self):
        if not self.caption.strip() or len(set(self.columns)) != len(self.columns):
            raise ValueError('A table needs a caption and distinct column headings')
        if any(len(row) != len(self.columns) for row in self.rows):
            raise ValueError('Every row must match the column count')
        return self
