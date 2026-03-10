from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.actividad_participante_schema import ActividadParticipanteCreate, ActividadParticipanteUpdate, ActividadParticipanteOut
from app.controllers import actividad_participante_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[ActividadParticipanteOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=ActividadParticipanteOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return obj

@router.get("/actividad/{actividad_id}", response_model=List[ActividadParticipanteOut])
async def por_actividad(actividad_id: int, db: AsyncSession = Depends(get_db)):
    return await ctrl.get_by_actividad(db, actividad_id)

@router.post("/", response_model=ActividadParticipanteOut, status_code=201)
async def crear(data: ActividadParticipanteCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.put("/{id}", response_model=ActividadParticipanteOut)
async def actualizar(id: int, data: ActividadParticipanteUpdate, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.update(db, id, data.model_dump(exclude_none=True))
    if not obj:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return obj

@router.delete("/{id}", response_model=ActividadParticipanteOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return obj