from pydantic import BaseModel
from typing import Optional
from datetime import date, time
from enum import Enum


class ActividadTipo(str, Enum):
    educativa   = "educativa"
    recreativa  = "recreativa"
    formativa   = "formativa"
    motriz      = "motriz"
    cultural    = "cultural"
    otra        = "otra"


class GrupoTipo(str, Enum):
    bebes        = "bebes"
    caminadores  = "caminadores"
    exploradores = "exploradores"
    preescolar   = "preescolar"


class ActividadCreate(BaseModel):
    titulo      : str
    descripcion : Optional[str]          = None
    tipo        : ActividadTipo          = ActividadTipo.educativa
    fecha       : date
    hora_inicio : Optional[time]         = None
    hora_fin    : Optional[time]         = None
    grupo       : Optional[GrupoTipo]    = None


class ActividadUpdate(BaseModel):
    titulo      : Optional[str]          = None
    descripcion : Optional[str]          = None
    tipo        : Optional[ActividadTipo] = None
    fecha       : Optional[date]         = None
    hora_inicio : Optional[time]         = None
    hora_fin    : Optional[time]         = None
    grupo       : Optional[GrupoTipo]    = None


class ActividadOut(BaseModel):
    id          : int
    titulo      : str
    descripcion : Optional[str]
    tipo        : ActividadTipo
    fecha       : date
    hora_inicio : Optional[time]
    hora_fin    : Optional[time]
    grupo       : Optional[GrupoTipo]

    class Config:
        from_attributes = True