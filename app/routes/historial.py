from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin
from app.controllers.historial_controller import (
    HistorialCreate, HistorialResponse, HistorialUpdate,
    create, delete, get_by_id, get_by_nino, update,
)

router = APIRouter()


@router.get("/nino/{nino_id}", response_model=list[HistorialResponse], summary="Historial por niño")
async def listar_historial(
    nino_id   : UUID,
    categoria : str | None = Query(default=None),
    db        : AsyncSession = Depends(get_db),
    _         : None = Depends(get_current_admin),
):
    return await get_by_nino(nino_id, db, categoria)


@router.post("/", response_model=HistorialResponse, status_code=201, summary="Crear registro")
async def crear_historial(
    data : HistorialCreate,
    db   : AsyncSession = Depends(get_db),
    _    : None = Depends(get_current_admin),
):
    return await create(data, db)


@router.put("/{historial_id}", response_model=HistorialResponse, summary="Actualizar registro")
async def actualizar_historial(
    historial_id : UUID,
    data         : HistorialUpdate,
    db           : AsyncSession = Depends(get_db),
    _            : None = Depends(get_current_admin),
):
    return await update(historial_id, data, db)


@router.delete("/{historial_id}", summary="Eliminar registro")
async def eliminar_historial(
    historial_id : UUID,
    db           : AsyncSession = Depends(get_db),
    _            : None = Depends(get_current_admin),
):
    return await delete(historial_id, db)