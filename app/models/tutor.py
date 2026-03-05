import uuid
from sqlalchemy import Boolean, Column, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

relacion_tipo = ENUM(
    'padre', 'madre', 'abuelo', 'abuela', 'tio', 'tia', 'tutor_legal', 'otro',
    name='relacion_tipo',
    create_type=False  # ya existe en Supabase, no la crea de nuevo
)

class Tutor(Base):
    __tablename__ = "tutores"

    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre              = Column(String(100), nullable=False)
    apellido            = Column(String(100), nullable=False)
    dni                 = Column(String(20), unique=True)
    telefono            = Column(String(20))
    telefono_emergencia = Column(String(20))
    email               = Column(String(150), unique=True)
    direccion           = Column(String)
    relacion            = Column(relacion_tipo, nullable=False, default="otro")
    activo              = Column(Boolean, default=True, nullable=False)
    creado_en           = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    # Relación con niños
    ninos = relationship("NinoTutor", back_populates="tutor")