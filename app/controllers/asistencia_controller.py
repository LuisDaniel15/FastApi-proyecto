from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.asistencia import Asistencia


async def get_all(db: AsyncSession):
    result = await db.execute(select(Asistencia))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, asistencia_id: int):
    result = await db.execute(select(Asistencia).where(Asistencia.id == asistencia_id))
    return result.scalar_one_or_none()


async def get_by_nino(db: AsyncSession, nino_id: int):
    result = await db.execute(select(Asistencia).where(Asistencia.nino_id == nino_id))
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    asistencia = Asistencia(**data)
    db.add(asistencia)
    await db.commit()
    await db.refresh(asistencia)
    return asistencia


async def update(db: AsyncSession, asistencia_id: int, data: dict):
    asistencia = await get_by_id(db, asistencia_id)
    if not asistencia:
        return None
    for key, value in data.items():
        setattr(asistencia, key, value)
    await db.commit()
    await db.refresh(asistencia)
    return asistencia


async def delete(db: AsyncSession, asistencia_id: int):
    asistencia = await get_by_id(db, asistencia_id)
    if not asistencia:
        return None
    await db.delete(asistencia)
    await db.commit()
    return asistencia