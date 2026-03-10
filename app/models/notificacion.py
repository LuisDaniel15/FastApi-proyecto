from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

notif_canal = ENUM(
    'email', 'sms', 'push', 'interna',
    name='notif_canal',
    create_type=False
)

notif_estado = ENUM(
    'pendiente', 'enviada', 'leida', 'fallida',
    name='notif_estado',
    create_type=False
)

class Notificacion(Base):
    __tablename__ = "notificaciones"

    id           = Column(Integer, primary_key=True, autoincrement=True)
    acudiente_id = Column(Integer, ForeignKey("acudientes.id", ondelete="CASCADE"), nullable=False)
    nino_id      = Column(Integer, ForeignKey("ninos.id",      ondelete="SET NULL"))
    titulo       = Column(String(200), nullable=False)
    mensaje      = Column(String, nullable=False)
    canal        = Column(notif_canal,  nullable=False, server_default="interna")
    estado       = Column(notif_estado, nullable=False, server_default="pendiente")
    enviada_en   = Column(TIMESTAMP(timezone=True))
    leida_en     = Column(TIMESTAMP(timezone=True))
    creado_en    = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    acudiente = relationship("Acudiente", back_populates="notificaciones")
    nino      = relationship("Nino")