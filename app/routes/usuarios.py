from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.db_config import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.controllers import usuario_controller as ctrl

router = APIRouter()

@router.get("/", response_model=List[UsuarioOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await ctrl.get_all(db)

@router.get("/{id}", response_model=UsuarioOut)
async def obtener(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return obj

@router.post("/", response_model=UsuarioOut, status_code=201)
async def crear(data: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    return await ctrl.create(db, data.model_dump())

@router.put("/{id}", response_model=UsuarioOut)
async def actualizar(id: int, data: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.update(db, id, data.model_dump(exclude_none=True))
    if not obj:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return obj

@router.delete("/{id}", response_model=UsuarioOut)
async def eliminar(id: int, db: AsyncSession = Depends(get_db)):
    obj = await ctrl.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return obj