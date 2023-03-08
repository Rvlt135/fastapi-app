import uuid
from typing import Optional

import shemas
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    user_name: str
    role_id: Optional[int] = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True


#
class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str  # Отправляем password в database.hash_password
    role_id: Optional[int] = 1
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

