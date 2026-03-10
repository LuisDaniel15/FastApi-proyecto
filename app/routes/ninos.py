from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.nino_schema import NinoCreate, NinoUpdate, NinoOut
from app.controllers import nino_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[NinoOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=NinoOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Niño no encontrado")
    return obj

@router.post("/", response_model=NinoOut, status_code=201)
async def crear(data: NinoCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.put("/{id}", response_model=NinoOut)
async def actualizar(id: int, data: NinoUpdate, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.update(db, id, data.model_dump(exclude_none=True))
    if not obj:
        raise HTTPException(status_code=404, detail="Niño no encontrado")
    return obj

@router.delete("/{id}", response_model=NinoOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Niño no encontrado")
    return obj