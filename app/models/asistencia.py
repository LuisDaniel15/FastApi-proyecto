from sqlalchemy import Column, Date, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

asistencia_estado = ENUM(
    'presente', 'ausente', 'tardanza', 'justificado',
    name='asistencia_estado',
    create_type=False
)

class Asistencia(Base):
    __tablename__ = "asistencia"

    id             = Column(Integer, primary_key=True, autoincrement=True)
    nino_id        = Column(Integer, ForeignKey("ninos.id",    ondelete="CASCADE"),  nullable=False)
    registrado_por = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    fecha          = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    hora_entrada   = Column(TIMESTAMP(timezone=True))
    hora_salida    = Column(TIMESTAMP(timezone=True))
    estado         = Column(asistencia_estado, nullable=False, server_default="presente")
    observacion    = Column(String)
    creado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino                   = relationship("Nino",    back_populates="asistencias")
    registrado_por_usuario = relationship("Usuario", back_populates="asistencias_registradas")