from pydantic import BaseModel


class HistorialNinoCreate(BaseModel):
    historial_id : int
    nino_id      : int


class HistorialNinoOut(BaseModel):
    id           : int
    historial_id : int
    nino_id      : int

    class Config:
        from_attributes = True