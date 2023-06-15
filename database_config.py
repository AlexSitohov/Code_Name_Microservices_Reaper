from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/users_db"

# create async engine for interaction with database
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# create session for the interaction with database
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, future=True)

Base = declarative_base()


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = SessionLocal()
        yield session
    finally:
        await session.close()
