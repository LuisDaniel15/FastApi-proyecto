from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.config.db_config import Base

class ActividadParticipante(Base):
    __tablename__ = "actividad_participantes"

    id           = Column(Integer, primary_key=True, autoincrement=True)
    actividad_id = Column(Integer, ForeignKey("actividades.id", ondelete="CASCADE"), nullable=False)
    nino_id      = Column(Integer, ForeignKey("ninos.id",       ondelete="CASCADE"), nullable=False)
    asistio      = Column(Boolean, nullable=False, server_default=text("TRUE"))
    observacion  = Column(String)
    creado_en    = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    actividad = relationship("Actividad", back_populates="participantes")
    nino      = relationship("Nino",      back_populates="actividades")