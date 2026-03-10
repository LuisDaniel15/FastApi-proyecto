from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.nino import Nino


async def get_all(db: AsyncSession):
    result = await db.execute(select(Nino).where(Nino.activo == True))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, nino_id: int):
    result = await db.execute(select(Nino).where(Nino.id == nino_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, data: dict):
    nino = Nino(**data)
    db.add(nino)
    await db.commit()
    await db.refresh(nino)
    return nino


async def update(db: AsyncSession, nino_id: int, data: dict):
    nino = await get_by_id(db, nino_id)
    if not nino:
        return None
    for key, value in data.items():
        setattr(nino, key, value)
    await db.commit()
    await db.refresh(nino)
    return nino


async def delete(db: AsyncSession, nino_id: int):
    nino = await get_by_id(db, nino_id)
    if not nino:
        return None
    nino.activo = False
    await db.commit()
    return nino