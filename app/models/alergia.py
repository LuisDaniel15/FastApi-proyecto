import uuid
from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

severidad_tipo = ENUM(
    'leve', 'moderada', 'severa',
    name='severidad_tipo',
    create_type=False
)

class Alergia(Base):
    __tablename__ = "alergias"

    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nino_id     = Column(UUID(as_uuid=True), ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    tipo        = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=False)
    severidad   = Column(severidad_tipo, nullable=False, default="moderada")
    creado_en   = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino = relationship("Nino", back_populates="alergias")