from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Parameter(BaseModel):
    parameterName: str
    parameterValue: Optional[str] = None
    parameterUnit: Optional[str] = None


class Time(BaseModel):
    startTime: datetime
    endTime: datetime
    parameter: Parameter


class WeatherElement(BaseModel):
    elementName: str
    time: List[Time]


class Location(BaseModel):
    locationName: str
    weatherElement: List[WeatherElement]


class Records(BaseModel):
    datasetDescription: str
    location: List[Location]


class FieldInfo(BaseModel):
    id: str
    type: str


class Result(BaseModel):
    resource_id: str
    fields: List[FieldInfo]


class WeatherResponse(BaseModel):
    success: str
    result: Result
    records: Records
