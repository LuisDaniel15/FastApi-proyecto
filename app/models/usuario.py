from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from app.config.db_config import Base

usuario_rol = ENUM(
    'admin', 'cuidador', 'auxiliar',
    name='usuario_rol',
    create_type=False
)

class Usuario(Base):
    __tablename__ = "usuarios"

    id             = Column(Integer, primary_key=True, autoincrement=True)
    nombre         = Column(String(100), nullable=False)
    apellido       = Column(String(100), nullable=False)
    email          = Column(String(150), nullable=False, unique=True)
    password_hash  = Column(String, nullable=True)
    rol            = Column(usuario_rol, nullable=False, server_default="cuidador")
    activo         = Column(Boolean, nullable=False, server_default=text("TRUE"))
    creado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

    asistencias_registradas = relationship("Asistencia",         back_populates="registrado_por_usuario")
    historiales             = relationship("Historial",          back_populates="autor")
    actividades             = relationship("ActividadPersonal",  back_populates="usuario")