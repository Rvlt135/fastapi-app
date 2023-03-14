from config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from contextlib import asynccontextmanager, contextmanager

async_engine = create_async_engine(settings.ASYNC_DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)
AsynSession = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

@asynccontextmanager
async def get_async_session():
    session = AsynSession()
    try:
        yield session
    except Exception as e:
        print(e)
        await session.rollback()
    finally:
        await session.close()


def async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper



@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def session_db(func):
    def wrapper(*args, **kwargs):
        with get_session() as session:
            return func(session, *args, **kwargs)
    return wrapper
"""
OLD
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
"""