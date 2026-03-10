from pydantic import BaseModel
from typing import Optional


class ActividadParticipanteCreate(BaseModel):
    actividad_id : int
    nino_id      : int
    asistio      : bool         = True
    observacion  : Optional[str] = None


class ActividadParticipanteUpdate(BaseModel):
    asistio     : Optional[bool] = None
    observacion : Optional[str]  = None


class ActividadParticipanteOut(BaseModel):
    id           : int
    actividad_id : int
    nino_id      : int
    asistio      : bool
    observacion  : Optional[str]

    class Config:
        from_attributes = True