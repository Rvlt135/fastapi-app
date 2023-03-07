# fastapi-app
Lessons fast-api

uvicorn app:app --reload
Runner: main

migration:
     alembic revision --autogenerate -m "commit"
     revision_id = cat migrations/versions/{file_migration}.revision
     alembic upgrade revision_id