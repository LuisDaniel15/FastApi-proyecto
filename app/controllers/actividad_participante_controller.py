from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.actividad_participante import ActividadParticipante


async def get_all(db: AsyncSession):
    result = await db.execute(select(ActividadParticipante))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ActividadParticipante).where(ActividadParticipante.id == id))
    return result.scalar_one_or_none()


async def get_by_actividad(db: AsyncSession, actividad_id: int):
    result = await db.execute(
        select(ActividadParticipante).where(ActividadParticipante.actividad_id == actividad_id)
    )
    return result.scalars().all()


async def create(db: AsyncSession, data: dict):
    participante = ActividadParticipante(**data)
    db.add(participante)
    await db.commit()
    await db.refresh(participante)
    return participante


async def update(db: AsyncSession, id: int, data: dict):
    participante = await get_by_id(db, id)
    if not participante:
        return None
    for key, value in data.items():
        setattr(participante, key, value)
    await db.commit()
    await db.refresh(participante)
    return participante


async def delete(db: AsyncSession, id: int):
    participante = await get_by_id(db, id)
    if not participante:
        return None
    await db.delete(participante)
    await db.commit()
    return participante