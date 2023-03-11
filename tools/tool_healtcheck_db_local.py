import psycopg2 as pgsql
from psycopg2 import OperationalError
from src.config import settings
try:
    # host local port docker
    connection = pgsql.connect(database=settings.POSTGRES_DB,
                               user=settings.POSTGRES_USER,
                               password=settings.POSTGRES_PASSWORD,
                               host=settings.POSTGRES_SERVER_DOCKER,
                               port=settings.POSTGRES_PORT)
    print('<h2>Подключение к базе данных выполнено успешно</h2>')
    connection.close()
except OperationalError as error:
    print(f'<h2>Ошибка подключения к БД: {error} </h2>')