from pydantic import BaseModel
from typing import Optional
from enum import Enum


class RolActividad(str, Enum):
    coordinador = "coordinador"
    apoyo       = "apoyo"
    observador  = "observador"


class ActividadPersonalCreate(BaseModel):
    actividad_id : int
    usuario_id   : int
    rol          : RolActividad = RolActividad.apoyo
    notas        : Optional[str] = None


class ActividadPersonalUpdate(BaseModel):
    rol   : Optional[RolActividad] = None
    notas : Optional[str]          = None


class ActividadPersonalOut(BaseModel):
    id           : int
    actividad_id : int
    usuario_id   : int
    rol          : RolActividad
    notas        : Optional[str]

    class Config:
        from_attributes = True