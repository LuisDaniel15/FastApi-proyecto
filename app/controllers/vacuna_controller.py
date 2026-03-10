from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.vacuna import Vacuna


async def get_all(db: AsyncSession):
    result = await db.execute(select(Vacuna))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, vacuna_id: int):
    result = await db.execute(select(Vacuna).where(Vacuna.id == vacuna_id))
    return result.scalar_one_or_none()


async def get_by_nino(db: AsyncSession, nino_id: int):
    result = await db.execute(select(Vacuna).where(Vacuna.nino_id == nino_id))
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    vacuna = Vacuna(**data)
    db.add(vacuna)
    await db.commit()
    await db.refresh(vacuna)
    return vacuna


async def update(db: AsyncSession, vacuna_id: int, data: dict):
    vacuna = await get_by_id(db, vacuna_id)
    if not vacuna:
        return None
    for key, value in data.items():
        setattr(vacuna, key, value)
    await db.commit()
    await db.refresh(vacuna)
    return vacuna


async def delete(db: AsyncSession, vacuna_id: int):
    vacuna = await get_by_id(db, vacuna_id)
    if not vacuna:
        return None
    await db.delete(vacuna)
    await db.commit()
    return vacuna