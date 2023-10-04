from enum import Enum
from typing import Optional, Tuple

from pydantic import BaseModel


class MeasureType(str, Enum):
    NUMBER = "number"
    SUM = "sum"
    COUNT = "count"


class DimensionType(str, Enum):
    NUMBER = "number"
    STRING = "string"
    TIMESTAMP = "time"


class Dimension(BaseModel):
    name: str
    type: DimensionType
    sql: str
    primary_key: bool = False


class Measure(BaseModel):
    name: str
    type: MeasureType
    sql: Optional[str]


class Cube(BaseModel):
    name: str
    dimensions: Tuple[Dimension, ...]
    measures: Tuple[Measure, ...]
