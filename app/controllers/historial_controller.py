from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.historial import Historial


async def get_all(db: AsyncSession):
    result = await db.execute(select(Historial))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, historial_id: int):
    result = await db.execute(select(Historial).where(Historial.id == historial_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, data: dict):
    registro = Historial(**data)
    db.add(registro)
    await db.commit()
    await db.refresh(registro)
    return registro


async def update(db: AsyncSession, historial_id: int, data: dict):
    registro = await get_by_id(db, historial_id)
    if not registro:
        return None
    for key, value in data.items():
        setattr(registro, key, value)
    await db.commit()
    await db.refresh(registro)
    return registro


async def delete(db: AsyncSession, historial_id: int):
    registro = await get_by_id(db, historial_id)
    if not registro:
        return None
    await db.delete(registro)
    await db.commit()
    return registro