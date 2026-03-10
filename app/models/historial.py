from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

historial_categoria = ENUM(
    'comportamiento', 'progreso', 'salud', 'incidente', 'logro', 'general',
    name='historial_categoria',
    create_type=False
)

class Historial(Base):
    __tablename__ = "historial"

    id                   = Column(Integer, primary_key=True, autoincrement=True)
    autor_id             = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    categoria            = Column(historial_categoria, nullable=False, server_default="general")
    titulo               = Column(String(200))
    descripcion          = Column(String, nullable=False)
    fecha                = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    medidas_tomadas      = Column(String)
    acudiente_notificado = Column(Boolean, nullable=False, server_default=text("FALSE"))
    es_privado           = Column(Boolean, nullable=False, server_default=text("FALSE"))
    creado_en            = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en       = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    autor = relationship("Usuario",      back_populates="historiales")
    ninos = relationship("HistorialNino", back_populates="historial")