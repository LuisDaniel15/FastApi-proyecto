from sqlalchemy import Column, Date, Integer, String, TIMESTAMP, Time, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

actividad_tipo = ENUM(
    'educativa', 'recreativa', 'formativa', 'motriz', 'cultural', 'otra',
    name='actividad_tipo',
    create_type=False
)

grupo_tipo = ENUM(
    'bebes', 'caminadores', 'exploradores', 'preescolar',
    name='grupo_tipo',
    create_type=False
)

class Actividad(Base):
    __tablename__ = "actividades"

    id             = Column(Integer, primary_key=True, autoincrement=True)
    titulo         = Column(String(200), nullable=False)
    descripcion    = Column(String)
    tipo           = Column(actividad_tipo, nullable=False, server_default="educativa")
    fecha          = Column(Date, nullable=False)
    hora_inicio    = Column(Time)
    hora_fin       = Column(Time)
    grupo          = Column(grupo_tipo)
    creado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    personal      = relationship("ActividadPersonal",     back_populates="actividad")
    participantes = relationship("ActividadParticipante", back_populates="actividad")