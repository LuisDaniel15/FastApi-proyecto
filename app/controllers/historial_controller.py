from datetime import date
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.historial import Historial


# ── Schemas ───────────────────────────────────────────────────────────────────
class HistorialCreate(BaseModel):
    nino_id     : UUID
    autor_id    : UUID | None = None
    categoria   : str = "general"
    titulo      : str | None = None
    descripcion : str
    fecha       : date | None = None
    es_privado  : bool = False


class HistorialUpdate(BaseModel):
    categoria   : str | None = None
    titulo      : str | None = None
    descripcion : str | None = None
    es_privado  : bool | None = None


class HistorialResponse(BaseModel):
    id          : UUID
    nino_id     : UUID
    autor_id    : UUID | None
    categoria   : str
    titulo      : str | None
    descripcion : str
    fecha       : date
    es_privado  : bool

    class Config:
        from_attributes = True


# ── CRUD ──────────────────────────────────────────────────────────────────────
async def get_by_nino(
    nino_id: UUID,
    db: AsyncSession,
    categoria: str | None = None,
) -> list[Historial]:
    query = select(Historial).where(Historial.nino_id == nino_id)
    if categoria:
        query = query.where(Historial.categoria == categoria)
    query = query.order_by(Historial.fecha.desc())
    result = await db.execute(query)
    return result.scalars().all()


async def get_by_id(historial_id: UUID, db: AsyncSession) -> Historial:
    result = await db.execute(select(Historial).where(Historial.id == historial_id))
    h = result.scalar_one_or_none()
    if not h:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado")
    return h


async def create(data: HistorialCreate, db: AsyncSession) -> Historial:
    h = Historial(**data.model_dump())
    db.add(h)
    await db.flush()
    await db.refresh(h)
    return h


async def update(historial_id: UUID, data: HistorialUpdate, db: AsyncSession) -> Historial:
    h = await get_by_id(historial_id, db)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(h, field, value)
    await db.flush()
    await db.refresh(h)
    return h


async def delete(historial_id: UUID, db: AsyncSession) -> dict:
    h = await get_by_id(historial_id, db)
    await db.delete(h)
    await db.flush()
    return {"mensaje": "Registro eliminado correctamente"}