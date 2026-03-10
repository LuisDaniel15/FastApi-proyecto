from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.notificacion import Notificacion


async def get_all(db: AsyncSession):
    result = await db.execute(select(Notificacion))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, notificacion_id: int):
    result = await db.execute(select(Notificacion).where(Notificacion.id == notificacion_id))
    return result.scalar_one_or_none()


async def get_by_acudiente(db: AsyncSession, acudiente_id: int):
    result = await db.execute(
        select(Notificacion).where(Notificacion.acudiente_id == acudiente_id)
    )
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    notificacion = Notificacion(**data)
    db.add(notificacion)
    await db.commit()
    await db.refresh(notificacion)
    return notificacion


async def update(db: AsyncSession, notificacion_id: int, data: dict):
    notificacion = await get_by_id(db, notificacion_id)
    if not notificacion:
        return None
    for key, value in data.items():
        setattr(notificacion, key, value)
    await db.commit()
    await db.refresh(notificacion)
    return notificacion


async def delete(db: AsyncSession, notificacion_id: int):
    notificacion = await get_by_id(db, notificacion_id)
    if not notificacion:
        return None
    await db.delete(notificacion)
    await db.commit()
    return notificacion