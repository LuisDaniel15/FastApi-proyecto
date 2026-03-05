import uuid
from sqlalchemy import Boolean, Column, Date, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM

from app.config.db_config import Base

rol_personal_tipo = ENUM(
    'director', 'pedagogo', 'cuidador', 'auxiliar', 'administrativo', 'otro',
    name='rol_personal_tipo',
    create_type=False
)

class Personal(Base):
    __tablename__ = "personal"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre        = Column(String(100), nullable=False)
    apellido      = Column(String(100), nullable=False)
    dni           = Column(String(20), unique=True)
    email         = Column(String(150), unique=True)
    telefono      = Column(String(20))
    rol           = Column(rol_personal_tipo, nullable=False, default="cuidador")
    especialidad  = Column(String(100))
    fecha_ingreso = Column(Date, server_default=text("CURRENT_DATE"))
    activo        = Column(Boolean, default=True, nullable=False)
    creado_en     = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en= Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))