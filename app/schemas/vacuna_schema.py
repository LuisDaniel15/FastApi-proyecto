from pydantic import BaseModel
from typing import Optional
from datetime import date


class VacunaCreate(BaseModel):
    nino_id          : int
    nombre           : str
    fecha_aplicacion : date
    proxima_dosis    : Optional[date] = None
    notas            : Optional[str]  = None


class VacunaUpdate(BaseModel):
    nombre           : Optional[str]  = None
    fecha_aplicacion : Optional[date] = None
    proxima_dosis    : Optional[date] = None
    notas            : Optional[str]  = None


class VacunaOut(BaseModel):
    id               : int
    nino_id          : int
    nombre           : str
    fecha_aplicacion : date
    proxima_dosis    : Optional[date]
    notas            : Optional[str]

    class Config:
        from_attributes = True