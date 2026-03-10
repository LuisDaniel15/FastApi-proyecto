from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import bcrypt

from app.models.usuario import Usuario


async def get_all(db: AsyncSession):
    result = await db.execute(select(Usuario).where(Usuario.activo == True))
    return result.scalars().all()


async def get_by_id(db: AsyncSession, usuario_id: int):
    result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    return result.scalar_one_or_none()


async def create(db: AsyncSession, data: dict):
    if "password" in data:
        data["password_hash"] = bcrypt.hashpw(
            data.pop("password").encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
    usuario = Usuario(**data)
    db.add(usuario)
    await db.commit()
    await db.refresh(usuario)
    return usuario


async def update(db: AsyncSession, usuario_id: int, data: dict):
    usuario = await get_by_id(db, usuario_id)
    if not usuario:
        return None
    for key, value in data.items():
        setattr(usuario, key, value)
    await db.commit()
    await db.refresh(usuario)
    return usuario


async def delete(db: AsyncSession, usuario_id: int):
    usuario = await get_by_id(db, usuario_id)
    if not usuario:
        return None
    usuario.activo = False
    await db.commit()
    return usuario