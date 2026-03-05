from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin
from app.controllers.nino_controller import (
    AlergiaCreate, AsignarTutorSchema, NinoCreate, NinoResponse, NinoUpdate, VacunaCreate,
    agregar_alergia, agregar_vacuna, asignar_tutor,
    create, delete, get_all, get_by_id, update,
)

router = APIRouter()


@router.get("/", response_model=list[NinoResponse], summary="Listar niños")
async def listar_ninos(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_all(db, skip, limit)


@router.get("/{nino_id}", response_model=NinoResponse, summary="Obtener niño por ID")
async def obtener_nino(
    nino_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_by_id(nino_id, db)


@router.post("/", response_model=NinoResponse, status_code=201, summary="Crear niño")
async def crear_nino(
    data: NinoCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await create(data, db)


@router.put("/{nino_id}", response_model=NinoResponse, summary="Actualizar niño")
async def actualizar_nino(
    nino_id: UUID,
    data: NinoUpdate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await update(nino_id, data, db)


@router.delete("/{nino_id}", summary="Desactivar niño")
async def desactivar_nino(
    nino_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await delete(nino_id, db)


@router.post("/{nino_id}/tutores", summary="Asignar tutor a niño")
async def asignar_tutor_a_nino(
    nino_id: UUID,
    data: AsignarTutorSchema,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await asignar_tutor(nino_id, data, db)


@router.post("/{nino_id}/alergias", summary="Agregar alergia a niño")
async def agregar_alergia_a_nino(
    nino_id: UUID,
    data: AlergiaCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await agregar_alergia(nino_id, data, db)


@router.post("/{nino_id}/vacunas", summary="Agregar vacuna a niño")
async def agregar_vacuna_a_nino(
    nino_id: UUID,
    data: VacunaCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await agregar_vacuna(nino_id, data, db)