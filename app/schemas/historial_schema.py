from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class HistorialCategoria(str, Enum):
    comportamiento = "comportamiento"
    progreso       = "progreso"
    salud          = "salud"
    incidente      = "incidente"
    logro          = "logro"
    general        = "general"


class HistorialCreate(BaseModel):
    autor_id             : Optional[int]              = None
    categoria            : HistorialCategoria         = HistorialCategoria.general
    titulo               : Optional[str]              = None
    descripcion          : str
    fecha                : Optional[date]             = None
    medidas_tomadas      : Optional[str]              = None
    acudiente_notificado : bool                       = False
    es_privado           : bool                       = False


class HistorialUpdate(BaseModel):
    categoria            : Optional[HistorialCategoria] = None
    titulo               : Optional[str]                = None
    descripcion          : Optional[str]                = None
    fecha                : Optional[date]               = None
    medidas_tomadas      : Optional[str]                = None
    acudiente_notificado : Optional[bool]               = None
    es_privado           : Optional[bool]               = None


class HistorialOut(BaseModel):
    id                   : int
    autor_id             : Optional[int]
    categoria            : HistorialCategoria
    titulo               : Optional[str]
    descripcion          : str
    fecha                : date
    medidas_tomadas      : Optional[str]
    acudiente_notificado : bool
    es_privado           : bool

    class Config:
        from_attributes = True