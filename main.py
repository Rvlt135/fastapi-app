from fastapi import FastAPI
from shemas import Strain


app = FastAPI()


@app.get('/')
def main():
    return {"status" : "OK"}


@app.get('/user/{user_id}/items/{item}')
def item(user_id: int, item: str = None):
    return {'pk': user_id, 'query': item}


@app.post('/api/strain/')
def post_strain(item: Strain):
    return item
