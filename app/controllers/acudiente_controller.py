from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.acudiente import Acudiente


async def get_all(db: AsyncSession):
    result = await db.execute(select(Acudiente).where(Acudiente.activo == True))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, acudiente_id: int):
    result = await db.execute(select(Acudiente).where(Acudiente.id == acudiente_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, data: dict):
    acudiente = Acudiente(**data)
    db.add(acudiente)
    await db.commit()
    await db.refresh(acudiente)
    return acudiente


async def update(db: AsyncSession, acudiente_id: int, data: dict):
    acudiente = await get_by_id(db, acudiente_id)
    if not acudiente:
        return None
    for key, value in data.items():
        setattr(acudiente, key, value)
    await db.commit()
    await db.refresh(acudiente)
    return acudiente


async def delete(db: AsyncSession, acudiente_id: int):
    acudiente = await get_by_id(db, acudiente_id)
    if not acudiente:
        return None
    acudiente.activo = False
    await db.commit()
    return acudiente