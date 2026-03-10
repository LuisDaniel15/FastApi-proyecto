from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class UsuarioRol(str, Enum):
    admin     = "admin"
    cuidador  = "cuidador"
    auxiliar  = "auxiliar"


class UsuarioCreate(BaseModel):
    nombre   : str
    apellido : str
    email    : EmailStr
    password : Optional[str] = None
    rol      : UsuarioRol = UsuarioRol.cuidador


class UsuarioUpdate(BaseModel):
    nombre   : Optional[str]       = None
    apellido : Optional[str]       = None
    email    : Optional[EmailStr]  = None
    rol      : Optional[UsuarioRol] = None
    activo   : Optional[bool]      = None


class UsuarioOut(BaseModel):
    id       : int
    nombre   : str
    apellido : str
    email    : str
    rol      : UsuarioRol
    activo   : bool

    class Config:
        from_attributes = True