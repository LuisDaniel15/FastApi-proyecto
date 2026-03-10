from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.actividad_personal import ActividadPersonal


async def get_all(db: AsyncSession):
    result = await db.execute(select(ActividadPersonal))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ActividadPersonal).where(ActividadPersonal.id == id))
    return result.scalar_one_or_none()


async def get_by_actividad(db: AsyncSession, actividad_id: int):
    result = await db.execute(
        select(ActividadPersonal).where(ActividadPersonal.actividad_id == actividad_id)
    )
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    registro = ActividadPersonal(**data)
    db.add(registro)
    await db.commit()
    await db.refresh(registro)
    return registro


async def update(db: AsyncSession, id: int, data: dict):
    registro = await get_by_id(db, id)
    if not registro:
        return None
    for key, value in data.items():
        setattr(registro, key, value)
    await db.commit()
    await db.refresh(registro)
    return registro


async def delete(db: AsyncSession, id: int):
    registro = await get_by_id(db, id)
    if not registro:
        return None
    await db.delete(registro)
    await db.commit()
    return registro