import uuid
from sqlalchemy import Boolean, Column, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID

from app.config.db_config import Base


class Admin(Base):
    __tablename__ = "admins"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre         = Column(String(100), nullable=False)
    email          = Column(String(150), nullable=False, unique=True)
    password_hash  = Column(String, nullable=False)
    activo         = Column(Boolean, default=True, nullable=False)
    creado_en      = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))