from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.notificacion_schema import NotificacionCreate, NotificacionUpdate, NotificacionOut
from app.controllers import notificacion_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[NotificacionOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=NotificacionOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return obj

@router.get("/acudiente/{acudiente_id}", response_model=List[NotificacionOut])
async def por_acudiente(acudiente_id: int, db: AsyncSession = Depends(get_db)):
    return await ctrl.get_by_acudiente(db, acudiente_id)

@router.post("/", response_model=NotificacionOut, status_code=201)
async def crear(data: NotificacionCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.put("/{id}", response_model=NotificacionOut)
async def actualizar(id: int, data: NotificacionUpdate, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.update(db, id, data.model_dump(exclude_none=True))
    if not obj:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return obj

@router.delete("/{id}", response_model=NotificacionOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return obj