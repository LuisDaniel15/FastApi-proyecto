from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.nino_acudiente import NinoAcudiente


async def get_all(db: AsyncSession):
    result = await db.execute(select(NinoAcudiente))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(NinoAcudiente).where(NinoAcudiente.id == id))
    return result.scalar_one_or_none()


async def get_by_nino(db: AsyncSession, nino_id: int):
    result = await db.execute(select(NinoAcudiente).where(NinoAcudiente.nino_id == nino_id))
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    relacion = NinoAcudiente(**data)
    db.add(relacion)
    await db.commit()
    await db.refresh(relacion)
    return relacion


async def update(db: AsyncSession, id: int, data: dict):
    relacion = await get_by_id(db, id)
    if not relacion:
        return None
    for key, value in data.items():
        setattr(relacion, key, value)
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