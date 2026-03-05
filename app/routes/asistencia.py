from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin
from app.controllers.asistencia_controller import (
    AsistenciaResponse, RegistrarEntradaSchema, RegistrarSalidaSchema,
    get_by_fecha, get_by_nino, registrar_entrada, registrar_salida,
)

router = APIRouter()


@router.post("/entrada", response_model=AsistenciaResponse, status_code=201, summary="Registrar entrada")
async def entrada(
    data: RegistrarEntradaSchema,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await registrar_entrada(data, db)


@router.put("/{asistencia_id}/salida", response_model=AsistenciaResponse, summary="Registrar salida")
async def salida(
    asistencia_id: UUID,
    data: RegistrarSalidaSchema,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await registrar_salida(asistencia_id, data, db)


@router.get("/fecha/{fecha}", response_model=list[AsistenciaResponse], summary="Asistencia por fecha")
async def por_fecha(
    fecha: date,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_by_fecha(fecha, db)


@router.get("/nino/{nino_id}", response_model=list[AsistenciaResponse], summary="Asistencia por niño")
async def por_nino(
    nino_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_by_nino(nino_id, db)