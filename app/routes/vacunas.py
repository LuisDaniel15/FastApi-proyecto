from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.vacuna_schema import VacunaCreate, VacunaUpdate, VacunaOut
from app.controllers import vacuna_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[VacunaOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=VacunaOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return obj

@router.get("/nino/{nino_id}", response_model=List[VacunaOut])
async def por_nino(nino_id: int, db: AsyncSession = Depends(get_db)):
    return await ctrl.get_by_nino(db, nino_id)

@router.post("/", response_model=VacunaOut, status_code=201)
async def crear(data: VacunaCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.put("/{id}", response_model=VacunaOut)
async def actualizar(id: int, data: VacunaUpdate, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.update(db, id, data.model_dump(exclude_none=True))
    if not obj:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return obj

@router.delete("/{id}", response_model=VacunaOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return obj