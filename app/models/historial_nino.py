from sqlalchemy import Column, ForeignKey, Integer, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.config.db_config import Base

class HistorialNino(Base):
    __tablename__ = "historial_ninos"

    id           = Column(Integer, primary_key=True, autoincrement=True)
    historial_id = Column(Integer, ForeignKey("historial.id", ondelete="CASCADE"), nullable=False)
    nino_id      = Column(Integer, ForeignKey("ninos.id",     ondelete="CASCADE"), nullable=False)
    creado_en    = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    historial = relationship("Historial", back_populates="ninos")
    nino      = relationship("Nino",      back_populates="historial")