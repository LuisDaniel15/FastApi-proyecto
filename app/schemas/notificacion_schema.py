from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class NotifCanal(str, Enum):
    email   = "email"
    sms     = "sms"
    push    = "push"
    interna = "interna"


class NotifEstado(str, Enum):
    pendiente = "pendiente"
    enviada   = "enviada"
    leida     = "leida"
    fallida   = "fallida"


class NotificacionCreate(BaseModel):
    acudiente_id : int
    nino_id      : Optional[int]      = None
    titulo       : str
    mensaje      : str
    canal        : NotifCanal         = NotifCanal.interna


class NotificacionUpdate(BaseModel):
    estado    : Optional[NotifEstado] = None
    leida_en  : Optional[datetime]   = None
    enviada_en: Optional[datetime]   = None


class NotificacionOut(BaseModel):
    id           : int
    acudiente_id : int
    nino_id      : Optional[int]
    titulo       : str
    mensaje      : str
    canal        : NotifCanal
    estado       : NotifEstado
    enviada_en   : Optional[datetime]
    leida_en     : Optional[datetime]

    class Config:
        from_attributes = True