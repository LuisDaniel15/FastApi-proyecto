from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.db_config import get_db
from app.controllers.auth_controller import get_current_admin, login
from app.models.admin import Admin


router = APIRouter()


@router.post("/login", summary="Login del administrador")
async def admin_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    return await login(form_data.username, form_data.password, db)


@router.get("/me", summary="Información del admin autenticado")
async def me(current_admin: Admin = Depends(get_current_admin)):
    return {
        "id":     str(current_admin.id),
        "nombre": current_admin.nombre,
        "email":  current_admin.email,
        "activo": current_admin.activo,
    }