from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.db_config import engine, Base
from app.models import (
    Usuario, Acudiente, Nino, NinoAcudiente,
    Alergia, Vacuna, Asistencia,
    Actividad, ActividadPersonal, ActividadParticipante,
    Historial, HistorialNino, Notificacion
)

from app.routes.usuarios               import router as usuarios_router
from app.routes.acudientes             import router as acudientes_router
from app.routes.ninos                  import router as ninos_router
from app.routes.nino_acudiente         import router as nino_acudiente_router
from app.routes.alergias               import router as alergias_router
from app.routes.vacunas                import router as vacunas_router
from app.routes.asistencia             import router as asistencia_router
from app.routes.actividades            import router as actividades_router
from app.routes.actividad_personal     import router as actividad_personal_router
from app.routes.actividad_participantes import router as actividad_participantes_router
from app.routes.historial              import router as historial_router
from app.routes.historial_ninos        import router as historial_ninos_router
from app.routes.notificaciones         import router as notificaciones_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Conexión a Supabase establecida")
    yield
    await engine.dispose()


app = FastAPI(
    title="Sistema Guardería",
    version="2.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router,               prefix="/usuarios",               tags=["Usuarios"])
app.include_router(acudientes_router,             prefix="/acudientes",             tags=["Acudientes"])
app.include_router(ninos_router,                  prefix="/ninos",                  tags=["Niños"])
app.include_router(nino_acudiente_router,         prefix="/nino-acudiente",         tags=["Niño-Acudiente"])
app.include_router(alergias_router,               prefix="/alergias",               tags=["Alergias"])
app.include_router(vacunas_router,                prefix="/vacunas",                tags=["Vacunas"])
app.include_router(asistencia_router,             prefix="/asistencia",             tags=["Asistencia"])
app.include_router(actividades_router,            prefix="/actividades",            tags=["Actividades"])
app.include_router(actividad_personal_router,     prefix="/actividad-personal",     tags=["Actividad Personal"])
app.include_router(actividad_participantes_router, prefix="/actividad-participantes", tags=["Actividad Participantes"])
app.include_router(historial_router,              prefix="/historial",              tags=["Historial"])
app.include_router(historial_ninos_router,        prefix="/historial-ninos",        tags=["Historial Niños"])
app.include_router(notificaciones_router,         prefix="/notificaciones",         tags=["Notificaciones"])