from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin
from app.controllers.tutor_controller import (
    TutorCreate, TutorResponse, TutorUpdate,
    create, delete, get_all, get_by_id, update,
)

router = APIRouter()


@router.get("/", response_model=list[TutorResponse], summary="Listar tutores")
async def listar_tutores(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_all(db, skip, limit)


@router.get("/{tutor_id}", response_model=TutorResponse, summary="Obtener tutor por ID")
async def obtener_tutor(
    tutor_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_by_id(tutor_id, db)


@router.post("/", response_model=TutorResponse, status_code=201, summary="Crear tutor")
async def crear_tutor(
    data: TutorCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await create(data, db)


@router.put("/{tutor_id}", response_model=TutorResponse, summary="Actualizar tutor")
async def actualizar_tutor(
    tutor_id: UUID,
    data: TutorUpdate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await update(tutor_id, data, db)


@router.delete("/{tutor_id}", summary="Desactivar tutor")
async def desactivar_tutor(
    tutor_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await delete(tutor_id, db)