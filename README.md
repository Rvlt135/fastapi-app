# fastapi-app + smoke_app
docker-compose up -d
uvicorn src.main:app --reload
Runner: main
migration:
     alembic revision --autogenerate 
     revision_id = cat migrations/versions/{file_migration}.revision
     alembic upgrade revision_id
