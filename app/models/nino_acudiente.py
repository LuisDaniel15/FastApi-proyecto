from sqlalchemy import Boolean, Column, ForeignKey, Integer, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.config.db_config import Base

class NinoAcudiente(Base):
    __tablename__ = "nino_acudiente"

    id                    = Column(Integer, primary_key=True, autoincrement=True)
    nino_id               = Column(Integer, ForeignKey("ninos.id",      ondelete="CASCADE"), nullable=False)
    acudiente_id          = Column(Integer, ForeignKey("acudientes.id", ondelete="CASCADE"), nullable=False)
    es_contacto_principal = Column(Boolean, nullable=False, server_default=text("FALSE"))
    puede_recoger         = Column(Boolean, nullable=False, server_default=text("TRUE"))
    creado_en             = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino      = relationship("Nino",      back_populates="acudientes")
    acudiente = relationship("Acudiente", back_populates="ninos")