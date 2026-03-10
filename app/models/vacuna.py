from sqlalchemy import Column, Date, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.config.db_config import Base

class Vacuna(Base):
    __tablename__ = "vacunas"

    id               = Column(Integer, primary_key=True, autoincrement=True)
    nino_id          = Column(Integer, ForeignKey("ninos.id", ondelete="CASCADE"), nullable=False)
    nombre           = Column(String(150), nullable=False)
    fecha_aplicacion = Column(Date, nullable=False)
    proxima_dosis    = Column(Date)
    notas            = Column(String)
    creado_en        = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    nino = relationship("Nino", back_populates="vacunas")