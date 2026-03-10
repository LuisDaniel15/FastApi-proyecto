from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


def get_db_url():
    return (
        "postgresql+asyncpg://"
        "postgres.ilbbknzbfbmzpzineojv:Supabase2026%2A"
        "@aws-0-us-west-2.pooler.supabase.com:5432/postgres"
    )


engine = create_async_engine(get_db_url(), echo=False)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session