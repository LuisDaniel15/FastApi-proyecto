from datetime import date
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.nino import Nino
from app.models.nino_tutor import NinoTutor
from app.models.alergia import Alergia
from app.models.vacuna import Vacuna


# ── Schemas ───────────────────────────────────────────────────────────────────
class NinoCreate(BaseModel):
    nombre                : str
    apellido              : str
    fecha_nacimiento      : date
    genero                : str | None = None
    foto_url              : str | None = None
    grupo                 : str | None = None
    tipo_sangre           : str | None = None
    medico_nombre         : str | None = None
    medico_telefono       : str | None = None
    seguro_medico         : str | None = None
    observaciones_medicas : str | None = None


class NinoUpdate(BaseModel):
    nombre                : str | None = None
    apellido              : str | None = None
    fecha_nacimiento      : date | None = None
    genero                : str | None = None
    foto_url              : str | None = None
    grupo                 : str | None = None
    activo                : bool | None = None
    tipo_sangre           : str | None = None
    medico_nombre         : str | None = None
    medico_telefono       : str | None = None
    seguro_medico         : str | None = None
    observaciones_medicas : str | None = None


class AlergiaCreate(BaseModel):
    tipo        : str
    descripcion : str
    severidad   : str = "moderada"


class VacunaCreate(BaseModel):
    nombre           : str
    fecha_aplicacion : date
    proxima_dosis    : date | None = None
    notas            : str | None = None


class AsignarTutorSchema(BaseModel):
    tutor_id              : UUID
    es_contacto_principal : bool = False
    puede_recoger         : bool = True


class NinoResponse(BaseModel):
    id                    : UUID
    nombre                : str
    apellido              : str
    fecha_nacimiento      : date
    genero                : str | None
    foto_url              : str | None
    grupo                 : str | None
    activo                : bool
    tipo_sangre           : str | None
    medico_nombre         : str | None
    medico_telefono       : str | None
    seguro_medico         : str | None
    observaciones_medicas : str | None

    class Config:
        from_attributes = True


# ── CRUD ──────────────────────────────────────────────────────────────────────
async def get_all(db: AsyncSession, skip: int = 0, limit: int = 20) -> list[Nino]:
    result = await db.execute(
        select(Nino).where(Nino.activo == True).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_by_id(nino_id: UUID, db: AsyncSession) -> Nino:
    result = await db.execute(
        select(Nino)
        .options(
            selectinload(Nino.tutores),
            selectinload(Nino.alergias),
            selectinload(Nino.vacunas),
        )
        .where(Nino.id == nino_id)
    )
    nino = result.scalar_one_or_none()
    if not nino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Niño no encontrado")
    return nino


async def create(data: NinoCreate, db: AsyncSession) -> Nino:
    nino = Nino(**data.model_dump())
    db.add(nino)
    await db.flush()
    await db.refresh(nino)
    return nino


async def update(nino_id: UUID, data: NinoUpdate, db: AsyncSession) -> Nino:
    result = await db.execute(select(Nino).where(Nino.id == nino_id))
    nino   = result.scalar_one_or_none()
    if not nino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Niño no encontrado")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(nino, field, value)
    await db.flush()
    await db.refresh(nino)
    return nino


async def delete(nino_id: UUID, db: AsyncSession) -> dict:
    result = await db.execute(select(Nino).where(Nino.id == nino_id))
    nino   = result.scalar_one_or_none()
    if not nino:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Niño no encontrado")
    nino.activo = False
    await db.flush()
    return {"mensaje": "Niño desactivado correctamente"}


async def asignar_tutor(nino_id: UUID, data: AsignarTutorSchema, db: AsyncSession) -> dict:
    # Verificar que no exista ya la relación
    result = await db.execute(
        select(NinoTutor).where(
            NinoTutor.nino_id  == nino_id,
            NinoTutor.tutor_id == data.tutor_id
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="El tutor ya está asignado a este niño")

    relacion = NinoTutor(
        nino_id               = nino_id,
        tutor_id              = data.tutor_id,
        es_contacto_principal = data.es_contacto_principal,
        puede_recoger         = data.puede_recoger,
    )
    db.add(relacion)
    await db.flush()
    return {"mensaje": "Tutor asignado correctamente"}


async def agregar_alergia(nino_id: UUID, data: AlergiaCreate, db: AsyncSession) -> Alergia:
    alergia = Alergia(nino_id=nino_id, **data.model_dump())
    db.add(alergia)
    await db.flush()
    await db.refresh(alergia)
    return alergia


async def agregar_vacuna(nino_id: UUID, data: VacunaCreate, db: AsyncSession) -> Vacuna:
    vacuna = Vacuna(nino_id=nino_id, **data.model_dump())
    db.add(vacuna)
    await db.flush()
    await db.refresh(vacuna)
    return vacuna