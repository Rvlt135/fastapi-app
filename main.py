import uvicorn
from fastapi import FastAPI, Query
from shemas import Strain

app = FastAPI()


@app.get('/healtcheck')
def healtcheck():
    return {"status" : "OK"}


@app.get('/api/strain/categories')
def get_list_categories():
    return {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}


@app.post('/api/strain/write')
def post_strain(item: Strain):
    return item


@app.get('/api/strain/')
def get_strain_name(q: str = Query(None, min_length=2, max_length=1000)):
    return q

"""
uvicorn.run(
    "main.app:app",
    # host=settings.server_host,
    # port=settings.server_port,
    reload=True,
)"""