from typing import List

import uvicorn
from fastapi import FastAPI, Query, Path, Body
from shemas import Strain, CategoriesStrain, User, StrainResult
import zlib
import hashlib

# encoding GeeksforGeeks using md5 hash
# function


app = FastAPI()


@app.get('/healtcheck')
def healtcheck():
    return {"status" : "OK"}


@app.get('/api/strain/categories')
def get_list_categories():
    return {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}


@app.post('/api/strain/write', response_model=Strain, response_model_exclude_unset=True,
          response_model_exclude={"description"})
def post_strain(strain: Strain):
    """
    string_starin_slug_hash = strain.slug_name
    result = hashlib.md5(string_starin_slug_hash.encode()).hexdigest()
    """
    """
    Разобраться с реализацией response_model
    @app.post('/api/strain/write', response_model=StrainResult, response_model_exclude={"description"})
    def post_strain(strain: Strain):
        string_starin_slug_hash = strain.slug_name
        result = hashlib.md5(string_starin_slug_hash.encode()).hexdigest()
        return {'data': StrainResult(**strain.dict(), id=3)}
        """
    return {'data': strain}
    # return {'data': StrainResult(**strain.dict(), id=3)}




@app.get('/api/strain/')
def get_strain_name(name: List[str] = Query(None, min_length=2, max_length=1000,description='query find name strain')):
    return name

"""
Примеры использования Path(), Query()
@app.get('/api/{test}')
def get_test_name(test: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=2, le=20, description="test test")):
    return {"pk": test, "pages": pages}"""


@app.post('/api/user', description="create user")
def create_user(data: str, user: User = Body(..., embed=True)):
    # Любые данные, которые мы хотим хешировать, представляются в виде байтовой строки
    # Хеш всегда одинаковый для одних и тех же данных
    byte_data = b'{data}'
    user_id = zlib.crc32(byte_data)
    return {"create user": user_id, "user": user}

"""
uvicorn.run(
    "main.app:app",
    # host=settings.server_host,
    # port=settings.server_port,
    reload=True,
)"""