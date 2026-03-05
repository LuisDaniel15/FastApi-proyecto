from datetime import date
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, datetime
from datetime import date, datetime
from app.models.asistencia import Asistencia


# ── Schemas ───────────────────────────────────────────────────────────────────
class RegistrarEntradaSchema(BaseModel):
    nino_id        : UUID
    estado         : str = "presente"
    registrado_por : UUID | None = None
    observacion    : str | None = None


class RegistrarSalidaSchema(BaseModel):
    observacion : str | None = None


class AsistenciaResponse(BaseModel):
    id             : UUID
    nino_id        : UUID
    fecha          : date
    hora_entrada   : datetime | None = None
    hora_salida    : datetime | None = None
    estado         : str
    registrado_por : UUID | None
    observacion    : str | None

    class Config:
        from_attributes = True


# ── CRUD ──────────────────────────────────────────────────────────────────────
async def registrar_entrada(data: RegistrarEntradaSchema, db: AsyncSession) -> Asistencia:
    # Verificar si ya tiene asistencia hoy
    result = await db.execute(
        select(Asistencia).where(
            Asistencia.nino_id == data.nino_id,
            Asistencia.fecha   == date.today()
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya se registró la entrada de este niño hoy"
        )

    from datetime import datetime, timezone
    asistencia = Asistencia(
        nino_id        = data.nino_id,
        estado         = data.estado,
        registrado_por = data.registrado_por,
        observacion    = data.observacion,
        hora_entrada   = datetime.now(timezone.utc),
    )
    db.add(asistencia)
    await db.flush()
    await db.refresh(asistencia)
    return asistencia


async def registrar_salida(asistencia_id: UUID, data: RegistrarSalidaSchema, db: AsyncSession) -> Asistencia:
    from datetime import datetime, timezone
    result = await db.execute(select(Asistencia).where(Asistencia.id == asistencia_id))
    asistencia = result.scalar_one_or_none()
    if not asistencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro de asistencia no encontrado")
    if asistencia.hora_salida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya se registró la salida de este niño")

    asistencia.hora_salida = datetime.now(timezone.utc)
    if data.observacion:
        asistencia.observacion = data.observacion
    await db.flush()
    await db.refresh(asistencia)
    return asistencia


async def get_by_fecha(fecha: date, db: AsyncSession) -> list[Asistencia]:
    result = await db.execute(
        select(Asistencia).where(Asistencia.fecha == fecha)
    )
    return result.scalars().all()


async def get_by_nino(nino_id: UUID, db: AsyncSession) -> list[Asistencia]:
    result = await db.execute(
        select(Asistencia)
        .where(Asistencia.nino_id == nino_id)
        .order_by(Asistencia.fecha.desc())
    )
    return result.scalars().all()