from datetime import date
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.personal import Personal


# ── Schemas ───────────────────────────────────────────────────────────────────
class PersonalCreate(BaseModel):
    nombre       : str
    apellido     : str
    dni          : str | None = None
    email        : EmailStr | None = None
    telefono     : str | None = None
    rol          : str = "cuidador"
    especialidad : str | None = None
    fecha_ingreso: date | None = None


class PersonalUpdate(BaseModel):
    nombre       : str | None = None
    apellido     : str | None = None
    dni          : str | None = None
    email        : EmailStr | None = None
    telefono     : str | None = None
    rol          : str | None = None
    especialidad : str | None = None
    activo       : bool | None = None


class PersonalResponse(BaseModel):
    id            : UUID
    nombre        : str
    apellido      : str
    dni           : str | None
    email         : str | None
    telefono      : str | None
    rol           : str
    especialidad  : str | None
    fecha_ingreso : date | None
    activo        : bool

    class Config:
        from_attributes = True


# ── CRUD ──────────────────────────────────────────────────────────────────────
async def get_all(db: AsyncSession, skip: int = 0, limit: int = 20) -> list[Personal]:
    result = await db.execute(
        select(Personal).where(Personal.activo == True).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_by_id(personal_id: UUID, db: AsyncSession) -> Personal:
    result = await db.execute(select(Personal).where(Personal.id == personal_id))
    p = result.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personal no encontrado")
    return p


async def create(data: PersonalCreate, db: AsyncSession) -> Personal:
    p = Personal(**data.model_dump())
    db.add(p)
    await db.flush()
    await db.refresh(p)
    return p


async def update(personal_id: UUID, data: PersonalUpdate, db: AsyncSession) -> Personal:
    p = await get_by_id(personal_id, db)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(p, field, value)
    await db.flush()
    await db.refresh(p)
    return p


async def delete(personal_id: UUID, db: AsyncSession) -> dict:
    p = await get_by_id(personal_id, db)
    p.activo = False
    await db.flush()
    return {"mensaje": "Personal desactivado correctamente"}