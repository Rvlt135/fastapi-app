import psycopg2 as pgsql
from psycopg2 import OperationalError
try:
    # host local port docker
    connection = pgsql.connect(database='postgres', user='user', password='123qwe', host='172.26.0.2', port='5432')
    print('<h2>Подключение к базе данных выполнено успешно</h2>')
    connection.close()
except OperationalError as error:
    print(f'<h2>Ошибка подключения к БД: {error} </h2>')