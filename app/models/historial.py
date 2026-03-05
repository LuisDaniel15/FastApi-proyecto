import uuid
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

historial_categoria = ENUM(
    'comportamiento', 'progreso', 'salud', 'incidente', 'logro', 'general',
    name='historial_categoria',
    create_type=False
)

class Historial(Base):
    __tablename__ = "historial"

    id           = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nino_id      = Column(UUID(as_uuid=True), ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    autor_id     = Column(UUID(as_uuid=True), ForeignKey("personal.id", ondelete="SET NULL"))
    categoria    = Column(historial_categoria, nullable=False, default="general")
    titulo       = Column(String(200))
    descripcion  = Column(String, nullable=False)
    fecha        = Column(Date, server_default=text("CURRENT_DATE"), nullable=False)
    es_privado   = Column(Boolean, default=False, nullable=False)
    creado_en    = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino     = relationship("Nino")
    personal = relationship("Personal")