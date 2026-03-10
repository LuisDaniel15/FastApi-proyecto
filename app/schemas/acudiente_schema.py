from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class RelacionTipo(str, Enum):
    padre       = "padre"
    madre       = "madre"
    abuelo      = "abuelo"
    abuela      = "abuela"
    tio         = "tio"
    tia         = "tia"
    tutor_legal = "tutor_legal"
    otro        = "otro"


class AcudienteCreate(BaseModel):
    nombre              : str
    apellido            : str
    dni                 : Optional[str]      = None
    telefono            : Optional[str]      = None
    telefono_emergencia : Optional[str]      = None
    email               : Optional[EmailStr] = None
    direccion           : Optional[str]      = None
    relacion            : RelacionTipo       = RelacionTipo.otro


class AcudienteUpdate(BaseModel):
    nombre              : Optional[str]        = None
    apellido            : Optional[str]        = None
    dni                 : Optional[str]        = None
    telefono            : Optional[str]        = None
    telefono_emergencia : Optional[str]        = None
    email               : Optional[EmailStr]   = None
    direccion           : Optional[str]        = None
    relacion            : Optional[RelacionTipo] = None
    activo              : Optional[bool]       = None


class AcudienteOut(BaseModel):
    id                  : int
    nombre              : str
    apellido            : str
    dni                 : Optional[str]
    telefono            : Optional[str]
    telefono_emergencia : Optional[str]
    email               : Optional[str]
    direccion           : Optional[str]
    relacion            : RelacionTipo
    activo              : bool

    class Config:
        from_attributes = True