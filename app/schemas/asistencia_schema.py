from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum


class AsistenciaEstado(str, Enum):
    presente    = "presente"
    ausente     = "ausente"
    tardanza    = "tardanza"
    justificado = "justificado"


class AsistenciaCreate(BaseModel):
    nino_id        : int
    registrado_por : Optional[int]              = None
    fecha          : Optional[date]             = None
    hora_entrada   : Optional[datetime]         = None
    hora_salida    : Optional[datetime]         = None
    estado         : AsistenciaEstado           = AsistenciaEstado.presente
    observacion    : Optional[str]              = None


class AsistenciaUpdate(BaseModel):
    registrado_por : Optional[int]              = None
    hora_entrada   : Optional[datetime]         = None
    hora_salida    : Optional[datetime]         = None
    estado         : Optional[AsistenciaEstado] = None
    observacion    : Optional[str]              = None


class AsistenciaOut(BaseModel):
    id             : int
    nino_id        : int
    registrado_por : Optional[int]
    fecha          : date
    hora_entrada   : Optional[datetime]
    hora_salida    : Optional[datetime]
    estado         : AsistenciaEstado
    observacion    : Optional[str]

    class Config:
        from_attributes = True