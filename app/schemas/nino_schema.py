from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class GeneroTipo(str, Enum):
    masculino = "masculino"
    femenino  = "femenino"
    otro      = "otro"


class GrupoTipo(str, Enum):
    bebes       = "bebes"
    caminadores = "caminadores"
    exploradores = "exploradores"
    preescolar  = "preescolar"


class NinoCreate(BaseModel):
    nombre                : str
    apellido              : str
    fecha_nacimiento      : date
    genero                : Optional[GeneroTipo] = None
    foto_url              : Optional[str]        = None
    grupo                 : Optional[GrupoTipo]  = None
    fecha_ingreso         : Optional[date]       = None
    tipo_sangre           : Optional[str]        = None
    medico_nombre         : Optional[str]        = None
    medico_telefono       : Optional[str]        = None
    seguro_medico         : Optional[str]        = None
    observaciones_medicas : Optional[str]        = None


class NinoUpdate(BaseModel):
    nombre                : Optional[str]        = None
    apellido              : Optional[str]        = None
    fecha_nacimiento      : Optional[date]       = None
    genero                : Optional[GeneroTipo] = None
    foto_url              : Optional[str]        = None
    grupo                 : Optional[GrupoTipo]  = None
    tipo_sangre           : Optional[str]        = None
    medico_nombre         : Optional[str]        = None
    medico_telefono       : Optional[str]        = None
    seguro_medico         : Optional[str]        = None
    observaciones_medicas : Optional[str]        = None
    activo                : Optional[bool]       = None


class NinoOut(BaseModel):
    id                    : int
    nombre                : str
    apellido              : str
    fecha_nacimiento      : date
    genero                : Optional[GeneroTipo]
    foto_url              : Optional[str]
    grupo                 : Optional[GrupoTipo]
    fecha_ingreso         : date
    activo                : bool
    tipo_sangre           : Optional[str]
    medico_nombre         : Optional[str]
    medico_telefono       : Optional[str]
    seguro_medico         : Optional[str]
    observaciones_medicas : Optional[str]

    class Config:
        from_attributes = True