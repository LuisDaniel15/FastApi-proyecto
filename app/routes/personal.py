from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin
from app.controllers.personal_controller import (
    PersonalCreate, PersonalResponse, PersonalUpdate,
    create, delete, get_all, get_by_id, update,
)

router = APIRouter()


@router.get("/", response_model=list[PersonalResponse], summary="Listar personal")
async def listar_personal(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_all(db, skip, limit)


@router.get("/{personal_id}", response_model=PersonalResponse, summary="Obtener personal por ID")
async def obtener_personal(
    personal_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await get_by_id(personal_id, db)


@router.post("/", response_model=PersonalResponse, status_code=201, summary="Crear personal")
async def crear_personal(
    data: PersonalCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await create(data, db)


@router.put("/{personal_id}", response_model=PersonalResponse, summary="Actualizar personal")
async def actualizar_personal(
    personal_id: UUID,
    data: PersonalUpdate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await update(personal_id, data, db)


@router.delete("/{personal_id}", summary="Desactivar personal")
async def desactivar_personal(
    personal_id: UUID,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(get_current_admin),
):
    return await delete(personal_id, db)