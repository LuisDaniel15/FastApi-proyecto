from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

severidad_tipo = ENUM(
    'leve', 'moderada', 'severa',
    name='severidad_tipo',
    create_type=False
)

class Alergia(Base):
    __tablename__ = "alergias"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    nino_id     = Column(Integer, ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    tipo        = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=False)
    severidad   = Column(severidad_tipo, nullable=False, server_default="moderada")
    creado_en   = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino = relationship("Nino", back_populates="alergias")