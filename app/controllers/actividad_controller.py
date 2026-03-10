from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.actividad import Actividad


async def get_all(db: AsyncSession):
    result = await db.execute(select(Actividad))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, actividad_id: int):
    result = await db.execute(select(Actividad).where(Actividad.id == actividad_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, data: dict):
    actividad = Actividad(**data)
    db.add(actividad)
    await db.commit()
    await db.refresh(actividad)
    return actividad


async def update(db: AsyncSession, actividad_id: int, data: dict):
    actividad = await get_by_id(db, actividad_id)
    if not actividad:
        return None
    for key, value in data.items():
        setattr(actividad, key, value)
    await db.commit()
    await db.refresh(actividad)
    return actividad


async def delete(db: AsyncSession, actividad_id: int):
    actividad = await get_by_id(db, actividad_id)
    if not actividad:
        return None
    await db.delete(actividad)
    await db.commit()
    return actividad