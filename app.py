from fastapi import FastAPI, Query, Body
from shemas import StrainInBySlugName, User, StrainOutBySlugName
import zlib
import hashlib
from typing import List

app = FastAPI()


@app.get('/healtcheck')
def healtcheck():
    return {"status": "OK"}


@app.get('/api/strain/categories')
def get_list_categories():
    return {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}


@app.post('/api/strain/write',
          response_model=StrainOutBySlugName,
          response_model_exclude_unset=True,
          response_model_include={"name", "slug_name", "strain_id"})
def post_strain(strain: StrainInBySlugName):
    """Принимает значения из модели Strain и возвращаетс StrainOut"""
    string_starin_slug_hash = strain.slug_name
    result = hashlib.md5(string_starin_slug_hash.encode()).hexdigest()

    return {**strain.dict(), "strain_id": result}
    # return {'data': StrainResult(**strain.dict(), id=3)}


@app.get('/api/strain/')
def get_strain_name(name: List[str] =
                    Query(None, min_length=2,
                          max_length=1000,
                          description='query find name strain')):
    return name


"""
Примеры использования Path(), Query()
@app.get('/api/{test}')
def get_test_name(test: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=2, le=20, description="test test")):
    return {"pk": test, "pages": pages}
"""


@app.post('/api/user', description="create user")
def create_user(data: str, user: User = Body(..., embed=True)):
    # Любые данные, которые мы хотим хешировать, представляются в виде байтовой строки
    # Хеш всегда одинаковый для одних и тех же данных
    byte_data = b'{data}'
    user_id = zlib.crc32(byte_data)
    return {"create user": user_id, "user": user}
