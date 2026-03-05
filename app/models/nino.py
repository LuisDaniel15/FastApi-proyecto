import uuid
from sqlalchemy import Boolean, Column, Date, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

genero_tipo = ENUM(
    'masculino', 'femenino', 'otro',
    name='genero_tipo',
    create_type=False
)

grupo_tipo = ENUM(
    'bebes', 'caminadores', 'exploradores', 'preescolar',
    name='grupo_tipo',
    create_type=False
)

class Nino(Base):
    __tablename__ = "ninos"

    id                    = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre                = Column(String(100), nullable=False)
    apellido              = Column(String(100), nullable=False)
    fecha_nacimiento      = Column(Date, nullable=False)
    genero                = Column(genero_tipo)
    foto_url              = Column(String)
    grupo                 = Column(grupo_tipo)
    fecha_ingreso         = Column(Date, server_default=text("CURRENT_DATE"))
    activo                = Column(Boolean, default=True, nullable=False)
    tipo_sangre           = Column(String(5))
    medico_nombre         = Column(String(150))
    medico_telefono       = Column(String(20))
    seguro_medico         = Column(String(100))
    observaciones_medicas = Column(String)
    creado_en             = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en        = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    # Relaciones
    tutores  = relationship("NinoTutor", back_populates="nino")
    alergias = relationship("Alergia",   back_populates="nino")
    vacunas  = relationship("Vacuna",    back_populates="nino")