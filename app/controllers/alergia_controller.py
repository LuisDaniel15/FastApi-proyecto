from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.alergia import Alergia


async def get_all(db: AsyncSession):
    result = await db.execute(select(Alergia))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, alergia_id: int):
    result = await db.execute(select(Alergia).where(Alergia.id == alergia_id))
    return result.scalar_one_or_none()


async def get_by_nino(db: AsyncSession, nino_id: int):
    result = await db.execute(select(Alergia).where(Alergia.nino_id == nino_id))
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    alergia = Alergia(**data)
    db.add(alergia)
    await db.commit()
    await db.refresh(alergia)
    return alergia


async def update(db: AsyncSession, alergia_id: int, data: dict):
    alergia = await get_by_id(db, alergia_id)
    if not alergia:
        return None
    for key, value in data.items():
        setattr(alergia, key, value)
    await db.commit()
    await db.refresh(alergia)
    return alergia


async def delete(db: AsyncSession, alergia_id: int):
    alergia = await get_by_id(db, alergia_id)
    if not alergia:
        return None
    await db.delete(alergia)
    await db.commit()
    return alergia