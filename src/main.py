import uvicorn
from fastapi import FastAPI
from src.categories.router import categories_router
from src.auth.router import router_auth
from strains.router import strain_router
from config import settings

app = FastAPI(
    title="Fast-api app"

)

app.include_router(categories_router)
app.include_router(router_auth)
app.include_router(strain_router)


@app.get('/healthcheck')
def health_check():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.server_host,
        port=settings.server_port,
        log_level="info",
        reload=True)

"""
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close() 
"""
