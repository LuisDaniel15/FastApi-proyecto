import uuid
from sqlalchemy import Boolean, Column, ForeignKey, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.config.db_config import Base


class NinoTutor(Base):
    __tablename__ = "nino_tutor"

    id                    = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nino_id               = Column(UUID(as_uuid=True), ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    tutor_id              = Column(UUID(as_uuid=True), ForeignKey("tutores.id", ondelete="CASCADE"), nullable=False)
    es_contacto_principal = Column(Boolean, default=False, nullable=False)
    puede_recoger         = Column(Boolean, default=True, nullable=False)
    creado_en             = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    # Relaciones
    nino  = relationship("Nino",  back_populates="tutores")
    tutor = relationship("Tutor", back_populates="ninos")