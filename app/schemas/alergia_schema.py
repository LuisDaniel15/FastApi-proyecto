from pydantic import BaseModel
from typing import Optional
from enum import Enum


class SeveridadTipo(str, Enum):
    leve     = "leve"
    moderada = "moderada"
    severa   = "severa"


class AlergiaCreate(BaseModel):
    nino_id     : int
    tipo        : str
    descripcion : str
    severidad   : SeveridadTipo = SeveridadTipo.moderada


class AlergiaUpdate(BaseModel):
    tipo        : Optional[str]          = None
    descripcion : Optional[str]          = None
    severidad   : Optional[SeveridadTipo] = None


class AlergiaOut(BaseModel):
    id          : int
    nino_id     : int
    tipo        : str
    descripcion : str
    severidad   : SeveridadTipo

    class Config:
        from_attributes = True