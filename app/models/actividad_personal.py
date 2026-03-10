from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

rol_actividad = ENUM(
    'coordinador', 'apoyo', 'observador',
    name='rol_actividad',
    create_type=False
)

class ActividadPersonal(Base):
    __tablename__ = "actividad_personal"

    id           = Column(Integer, primary_key=True, autoincrement=True)
    actividad_id = Column(Integer, ForeignKey("actividades.id", ondelete="CASCADE"), nullable=False)
    usuario_id   = Column(Integer, ForeignKey("usuarios.id",    ondelete="CASCADE"), nullable=False)
    rol          = Column(rol_actividad, nullable=False, server_default="apoyo")
    notas        = Column(String)
    creado_en    = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    actividad = relationship("Actividad", back_populates="personal")
    usuario   = relationship("Usuario",   back_populates="actividades")