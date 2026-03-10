from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.historial_nino import HistorialNino


async def get_all(db: AsyncSession):
    result = await db.execute(select(HistorialNino))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HistorialNino).where(HistorialNino.id == id))
    return result.scalar_one_or_none()


async def get_by_historial(db: AsyncSession, historial_id: int):
    result = await db.execute(
        select(HistorialNino).where(HistorialNino.historial_id == historial_id)
    )
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    relacion = HistorialNino(**data)
    db.add(relacion)
    await db.commit()
    await db.refresh(relacion)
    return relacion


async def delete(db: AsyncSession, id: int):
    relacion = await get_by_id(db, id)
    if not relacion:
        return None
    await db.delete(relacion)
    await db.commit()
    return relacion