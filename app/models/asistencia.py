import uuid
from sqlalchemy import Column, Date, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

asistencia_estado = ENUM(
    'presente', 'ausente', 'tardanza', 'justificado',
    name='asistencia_estado',
    create_type=False
)

class Asistencia(Base):
    __tablename__ = "asistencia"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nino_id        = Column(UUID(as_uuid=True), ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    fecha          = Column(Date, server_default=text("CURRENT_DATE"), nullable=False)
    hora_entrada   = Column(TIMESTAMP(timezone=True))
    hora_salida    = Column(TIMESTAMP(timezone=True))
    estado         = Column(asistencia_estado, nullable=False, default="presente")
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("personal.id", ondelete="SET NULL"))
    observacion    = Column(String)
    creado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino     = relationship("Nino")
    personal = relationship("Personal")