from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Supabase ---
    DATABASE_URL: str

    # --- JWT ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- App ---
    APP_NAME: str = "Sistema de Gestión Guardería"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()