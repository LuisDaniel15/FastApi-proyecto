from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.db_config import engine, Base
from app.config.settings import settings
from app.models import admin, tutor, nino, nino_tutor, alergia, vacuna, personal, asistencia, historial

from app.routes.auth import router as auth_router
from app.routes.tutores import router as tutores_router
from app.routes.ninos import router as ninos_router
from app.routes.personal import router as personal_router
from app.routes.asistencia import router as asistencia_router
from app.routes.historial import router as historial_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Conexión a Supabase establecida")
    yield
    await engine.dispose()
    print("🔌 Conexión a Supabase cerrada")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,       prefix="/auth",       tags=["Autenticación"])
app.include_router(tutores_router,    prefix="/tutores",    tags=["Tutores"])
app.include_router(ninos_router,      prefix="/ninos",      tags=["Niños"])
app.include_router(personal_router,   prefix="/personal",   tags=["Personal"])
app.include_router(asistencia_router, prefix="/asistencia", tags=["Asistencia"])
app.include_router(historial_router,  prefix="/historial",  tags=["Historial"])


@app.get("/", tags=["Health"])
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "online"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)