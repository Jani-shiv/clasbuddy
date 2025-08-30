from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import settings
import logging

logger = logging.getLogger(__name__)

# Determine if we're using async database or not
ASYNC_DATABASE_URL = None
if settings.database_url.startswith("postgresql://"):
    ASYNC_DATABASE_URL = settings.database_url.replace("postgresql://", "postgresql+asyncpg://")
elif settings.database_url.startswith("mysql://"):
    ASYNC_DATABASE_URL = settings.database_url.replace("mysql://", "mysql+aiomysql://")

# Create engines
if settings.database_url.startswith("sqlite"):
    engine = create_engine(
        settings.database_url, 
        connect_args={"check_same_thread": False}
    )
    async_engine = None
else:
    engine = create_engine(settings.database_url)
    async_engine = create_async_engine(ASYNC_DATABASE_URL) if ASYNC_DATABASE_URL else None

# Session makers
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(
    async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
) if async_engine else None

Base = declarative_base()

# Database dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    if AsyncSessionLocal is None:
        raise RuntimeError("Async database not configured")
    async with AsyncSessionLocal() as session:
        yield session

# Database initialization
def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")

def drop_tables():
    """Drop all tables in the database"""
    Base.metadata.drop_all(bind=engine)
    logger.info("Database tables dropped successfully")
