
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from src.database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


"""
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close() 
"""
