from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi_users import FastAPIUsers
from starlette import status
from starlette.requests import Request

from auth.schemas import UserRead, UserCreate
from shemas import CategoriesStrain, Strain, StrainDetails, CategoriesList
# import zlib
import hashlib
from typing import List
from auth.database import User
from auth.auth import auth_backend
from auth.manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="Fast-api app"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder({"detail": exc.errors()})
                        )


fake_categories_by_strain = [
    {"id": 1, "category_name": "Indica", "strain_id": "5be017ac85e474c239bb0ad5", "strain_slug": "purple-punch"},
    {"id": 2, "category_name": "Sativa", "strain_id": "5be0181985e474c239bb0def", "strain_slug": "jack-herer"},
    {"id": 3, "category_name": "Hybrid", "strains":
        [{"strain_id": "5be0181985e474c239bb01244", "strain_slug": "blue-dream"}, ]},
]

fake_categories_list = [
    {"id": 1, "category": "Indica"},
    {"id": 2, "category": "Sativa"},
    {"id": 3, "category": "Hybrid"},
]

fake_strains = [
    {"id": 1, "slug_name": "test_strain", "name": "Test Strain", "category": " Sativa",
     "hash_id": "test_hash"},
    {"id": 2, "slug_name": "test_slug_2", "name": "Test Name 2", "category": "Indica",
     "hash_id": "test_hash_2"}
]

fake_strain_list = [
    {"id": 1, "slug_name": "test_strain", "name": "Test Strain", "category": "Sativa",
     "hash_id": "test_hash"},
    {"id": 2, "slug_name": "test_slug_2", "name": "Test Name 2", "category": "Indica",
     "hash_id": "test_hash_2"},
]

clear_strain_list = []

"""def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()"""


@app.get('/healtcheck')
def healtcheck():
    return {"status": "OK"}


@app.post('/api/strain/add')
def add_strain(strain: List[Strain]):
    """Create strain and hashed hash_id"""
    for it in strain:
        string_starin_slug_hash = it.slug_name
        result_hash = hashlib.md5(string_starin_slug_hash.encode()).hexdigest()
        it.hash_id = result_hash
        fake_strain_list.extend(strain)
        clear_strain_list.extend(strain)
        # fake_strain.extend(strain)
    return fake_strain_list


@app.get('/api/strain/list', response_model=List[Strain])
def get_strain_list():
    return fake_strain_list


@app.get('/api/strain/', response_model=StrainDetails)
def get_strain(strain_id: int):
    for strain in fake_strain_list:
        # strain_dict = strain.dict()
        if strain.get("id") == strain_id:
            return strain


@app.get("/api/categories", response_model=List[CategoriesList])
def get_categories():
    return fake_categories_list


@app.get('/api/categories/byStrain', response_model=CategoriesStrain)
def get_categories_by_strains(get_id: int):
    """Принимает get_id возвращает несколько вариантов strains old and new"""

    for category_id in fake_categories_by_strain:
        if category_id.get("id") == get_id:
            return category_id


"""
Примеры использования Path(), Query()
@app.get('/api/{test}')
def get_test_name(test: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=2, le=20, description="test test")):
    return {"pk": test, "pages": pages}

@app.get('/api/strain/{id}')
def get_strain_name(name: List[str] =
                    Query(None, min_length=2,
                          max_length=1000,
                          description='query find name strain')):
    return name

@app.post('/api/user', description="create user")
def create_user(data: str, user: User = Body(..., embed=True)):
    # Любые данные, которые мы хотим хешировать, представляются в виде байтовой строки
    # Хеш всегда одинаковый для одних и тех же данных
    byte_data = b'{data}'
    user_id = zlib.crc32(byte_data)
    return {"create user": user_id, "user": user}
    """
