from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

relacion_tipo = ENUM(
    'padre', 'madre', 'abuelo', 'abuela', 'tio', 'tia', 'tutor_legal', 'otro',
    name='relacion_tipo',
    create_type=False
)

class Acudiente(Base):
    __tablename__ = "acudientes"

    id                  = Column(Integer, primary_key=True, autoincrement=True)
    nombre              = Column(String(100), nullable=False)
    apellido            = Column(String(100), nullable=False)
    dni                 = Column(String(20), unique=True)
    telefono            = Column(String(20))
    telefono_emergencia = Column(String(20))
    email               = Column(String(150), unique=True)
    direccion           = Column(String)
    relacion            = Column(relacion_tipo, nullable=False, server_default="otro")
    activo              = Column(Boolean, nullable=False, server_default=text("TRUE"))
    creado_en           = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    ninos          = relationship("NinoAcudiente", back_populates="acudiente")
    notificaciones = relationship("Notificacion",  back_populates="acudiente")