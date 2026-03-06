from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tutor import Tutor


# ── Schemas ───────────────────────────────────────────────────────────────────
class TutorCreate(BaseModel):
    nombre              : str
    apellido            : str
    dni                 : str | None = None
    telefono            : str | None = None
    telefono_emergencia : str | None = None
    email               : EmailStr | None = None
    direccion           : str | None = None
    relacion            : str = "otro"


class TutorUpdate(BaseModel):
    nombre              : str | None = None
    apellido            : str | None = None
    dni                 : str | None = None
    telefono            : str | None = None
    telefono_emergencia : str | None = None
    email               : EmailStr | None = None
    direccion           : str | None = None
    relacion            : str | None = None
    activo              : bool | None = None


class TutorResponse(BaseModel):
    id                  : UUID
    nombre              : str
    apellido            : str
    dni                 : str | None
    telefono            : str | None
    telefono_emergencia : str | None
    email               : str | None
    direccion           : str | None
    relacion            : str
    activo              : bool

    class Config:
        from_attributes = True


async def get_all(db: AsyncSession, skip: int = 0, limit: int = 20) -> list[Tutor]:
    result = await db.execute(
        select(Tutor).where(Tutor.activo == True).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_by_id(tutor_id: UUID, db: AsyncSession) -> Tutor:
    result = await db.execute(select(Tutor).where(Tutor.id == tutor_id))
    tutor  = result.scalar_one_or_none()
    if not tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor no encontrado")
    return tutor


async def create(data: TutorCreate, db: AsyncSession) -> Tutor:
    tutor = Tutor(**data.model_dump())
    db.add(tutor)
    await db.flush()
    await db.refresh(tutor)
    return tutor


async def update(tutor_id: UUID, data: TutorUpdate, db: AsyncSession) -> Tutor:
    tutor = await get_by_id(tutor_id, db)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(tutor, field, value)
    await db.flush()
    await db.refresh(tutor)
    return tutor


async def delete(tutor_id: UUID, db: AsyncSession) -> dict:
    tutor = await get_by_id(tutor_id, db)
    tutor.activo = False
    await db.flush()
    return {"mensaje": "Tutor desactivado correctamente"}