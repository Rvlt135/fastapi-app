from fastapi_users import FastAPIUsers
from fastapi import APIRouter
from src.auth.config import auth_backend
from src.auth.utils import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

router_auth = APIRouter(
    tags=["auth"]

)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router_auth.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt"
)

router_auth.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)

current_user = fastapi_users.current_user()