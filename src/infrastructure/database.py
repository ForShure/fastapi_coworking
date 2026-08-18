from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/coworking_db"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()