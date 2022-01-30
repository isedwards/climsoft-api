from typing import List, Optional
from pydantic import constr
from climsoft_api.api.schema import BaseSchema


class CreateStation(BaseSchema):
    stationId: constr(max_length=255)
    stationName: constr(max_length=255)
    wmoid: Optional[constr(max_length=20)]
    icaoid: Optional[constr(max_length=20)]
    latitude: float
    qualifier: Optional[constr(max_length=20)]
    longitude: float
    elevation: constr(max_length=255)
    geoLocationMethod: Optional[constr(max_length=255)]
    geoLocationAccuracy: Optional[float]
    openingDatetime: Optional[str]
    closingDatetime: str
    country: constr(max_length=50)
    authority: Optional[constr(max_length=255)]
    adminRegion: Optional[constr(max_length=255)]
    drainageBasin: Optional[constr(max_length=255)]
    wacaSelection: bool
    cptSelection: bool
    stationOperational: bool


class UpdateStation(BaseSchema):
    stationName: constr(max_length=255)
    wmoid: Optional[constr(max_length=20)]
    icaoid: Optional[constr(max_length=20)]
    latitude: float
    qualifier: Optional[constr(max_length=20)]
    longitude: float
    elevation: constr(max_length=255)
    geoLocationMethod: Optional[constr(max_length=255)]
    geoLocationAccuracy: Optional[float]
    openingDatetime: Optional[str]
    closingDatetime: str
    country: constr(max_length=50)
    authority: Optional[constr(max_length=255)]
    adminRegion: Optional[constr(max_length=255)]
    drainageBasin: Optional[constr(max_length=255)]
    wacaSelection: bool
    cptSelection: bool
    stationOperational: bool


class Station(CreateStation):
    openingDatetime: Optional[str]
    closingDatetime: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class StationResponse(BaseSchema):
    result: List[Station]
    message: str
    status: str