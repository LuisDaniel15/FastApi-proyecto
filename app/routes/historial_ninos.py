from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.historial_nino_schema import HistorialNinoCreate, HistorialNinoOut
from app.controllers import historial_nino_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[HistorialNinoOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=HistorialNinoOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return obj

@router.get("/historial/{historial_id}", response_model=List[HistorialNinoOut])
async def por_historial(historial_id: int, db: AsyncSession = Depends(get_db)):
    return await ctrl.get_by_historial(db, historial_id)

@router.post("/", response_model=HistorialNinoOut, status_code=201)
async def crear(data: HistorialNinoCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.delete("/{id}", response_model=HistorialNinoOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return obj