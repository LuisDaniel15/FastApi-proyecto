from pydantic import BaseModel
from typing import Optional


class NinoAcudienteCreate(BaseModel):
    nino_id               : int
    acudiente_id          : int
    es_contacto_principal : bool = False
    puede_recoger         : bool = True


class NinoAcudienteUpdate(BaseModel):
    es_contacto_principal : Optional[bool] = None
    puede_recoger         : Optional[bool] = None


class NinoAcudienteOut(BaseModel):
    id                    : int
    nino_id               : int
    acudiente_id          : int
    es_contacto_principal : bool
    puede_recoger         : bool

    class Config:
        from_attributes = True