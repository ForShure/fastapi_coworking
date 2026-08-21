from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

POSTGRES_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/coworking_db"

engine = create_async_engine(POSTGRES_DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)

async def get_db():
    session = async_session_maker()
    try:
        yield session
    finally:
        await session.close()
