from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    user_name: str
    role_id: Optional[int] = 1

    class Config:
        orm_mode = True


#
class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str  # Отправляем password в database.hash_password
    role_id: Optional[int] = 1

